FROM ubuntu:16:04

ENV LANG=C.UTF-8

RUN apt-get update && \
    apt-get install -y python3 python3-pip uwsgi uwsgi-plugin-python3 \
        nginx supervisor gosu rsyslog \
        libldap2-dev libsasl2-dev libmariadb-dev-compat \
        texlive-latex-extra texlive-fonts-recommended texlive-lang-german && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /usr/share/doc/* && \
    # add user, some directories and fix owners
    useradd --shell /bin/bash --home-dir /helfertool2 --create-home helfertool2 --uid 1000 && \
    mkdir /data /log /helfertool2/run && \
    chown -R helfertool2:helfertool2 /data /log /helfertool/run

COPY src /helfertool2/src
COPY deployment/docker/helfertool.sh /usr/local/bin/helfertool2
COPY deployment/docker/uwsgi.conf /helfertool2/uwsgi.conf
COPY deployment/docker/supervisord.conf /helfertool2/supervisord.conf
COPY deployment/docker/nginx.conf /helfertool2/nginx.conf
COPY deployment/docker/rsyslog.conf /helfertool2/rsyslog.conf

RUN cd /helfertool2/src/ && \
    # install python libs
    pip3 install -r requirements.txt mysqlclient psycopg2-binary uwsgitop && \
    # copy static files
    HELFERTOOL_CONFIG_FILE=/dev/null python3 manage.py collectstatic --noinput && \
    chmod -R go+rX /helfertool2/static && \
    # fix permissions
    chmod +x /usr/local/bin/helfertool2


VOLUME ["/config", "/data", "/log"]
EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/helfertool2"]
CMD ["run"]
