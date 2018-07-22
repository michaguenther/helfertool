#!/bin/bash

set -Eeo pipefail

# set default id/gid and drop privileges
: ${USERID:=1000}
: ${GROUPID:=1000}

if [ "$USERID" = "0" ] ; then
    echo "Running as root is not recommended. Exiting."
    exit 1
fi

if [ "$(id -u)" = "0" ] ; then
    chown -R $USERID:$GROUPID /var/lib/nginx /var/log/nginx /usr/share/nginx /helfertool/run
    exec gosu $USERID:$GROUPID "$BASH_SOURCE" "$@"
fi

# prepare environment
cd /helfertool/src
mkdir -p /data/media
export HELFERTOOL_CONFIG_FILE="/config/helfertool.yaml"

# command: init
if [ "$1" = "init" ] ; then
    # initialise database with default settings
    python3 manage.py migrate --noinput
    python3 manage.py loaddata toolsettings
    python3 manage.py createsuperuser

# command: createadmin
elif [ "$1" = "createadmin" ] ; then
    # create new superuser
    python3 manage.py migrate --noinput
    python3 manage.py createsuperuser

# command: reload
elif [ "$1" = "reload" ] ; then
    # reload uwsgi and celery
    touch /helfertool/uwsgi_reload

    if [ -f "/helfertool/celery.pid" ] ; then
        kill -HUP $(cat /helfertool/celery.pid)
    fi
# command: manage
elif [ "$1" = "init" ] ; then
    shift
    python3 manage.py $@
# command: run
elif [ "$1" = "run" ] ; then
    # input parameters
    if [ -z "$HELFERTOOL_WORKERS" ] ; then
        export HELFERTOOL_WORKERS="$(( 2 * $(nproc --all) ))"
    fi

    if [ -z "$HELFERTOOL_TASK_WORKERS" ] ; then
        task_workers="$(( $(nproc --all) / 2 ))"
        if [ "$task_workers" = "0" ] ; then
            task_workers=1
        fi

        export HELFERTOOL_TASK_WORKERS="$task_workers"
    fi

    echo "Running with $HELFERTOOL_WORKERS web and $HELFERTOOL_TASK_WORKERS task workers"

    # run migrations and go
    python3 manage.py migrate --noinput
    exec supervisord --nodaemon --configuration /helfertool/supervisord.conf

# help message
else
    echo "Commands: init, createadmin, reload, run, manage"
    exit 1
fi