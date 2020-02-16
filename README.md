Build cmd: 

    sudo docker build -t ikom/helfertool .
Run cmd: 

    sudo docker run -v /home/docker/ikom/helfertool/test/docker/config:/config -v /home/docker/ikom/helfertool/test/docker/data:/data -v /home/docker/ikom/helfertool/test/docker/log:/log -p 127.0.0.1:9000:8000 ikom/helfertool
    
     sudo docker run -v "$PWD/test/docker/config:/config" -p 127.0.0.1:9000:8000 ikom/helfertool
Run cmd (Daemon): 

    sudo docker run -d --name helfertool -v /home/docker/ikom/helfertool/test/docker/config:/config -v /home/docker/ikom/helfertool/test/docker/data:/data -v /home/docker/ikom/helfertool/test/docker/log:/log -p 127.0.0.1:9000:8000 ikom/helfertool

Helfertool is a Python3 and Django based tool that allows to manage the
volunteers or staff for an event.

See <https://www.helfertool.org> for more information.

# Install

Please have a look at the
[admin guide](https://docs.helfertool.org/admin/index.html)
in our documentation.

# Environment for development

A Python virtual environment should be used for development:

    python3 -m venv venv

The necessary Python libraries are listed in ``src/requirements.txt``:

    pip install -r src/requirements.txt

## Database

To create the SQLite database for testing, run:

    cd src
    python manage.py migrate
    python manage.py createcachetable
    
 Update the structure of the database 
 
    python manage.py makemigrations
    python manage.py migrate

## Runserver

Start the webserver for development:

    cd src
    python manage.py runserver

Now visit http://localhost:8000 with your browser.


## Celery and RabbitMQ

When working on a part of the Helfertool that uses Celery, a RabbitMQ instance
needs to be started:

RabbitMQ can be installed using Docker (note: the RabbitMQ server listens
on port 5672 to every incoming connection, you should configure a firewall):

    docker run -d --rm --hostname helfertool-rabbitmq --name helfertool-rabbitmq \
        -p 5672:5672 rabbitmq

The default settings in ``helfertool.yaml`` do not need to be changed.

Now start celery:

    cd src
    celery -A helfertool worker --loglevel=info -B

The celery worker here has the celery beat service included (``-B``).
This is not recommended for production (see [celery documentation](https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#id7))!

## Mails

The Helfertool tries to send mails to localhost:25 with the default
configuration.

If you want to test the E-Mail part during development, you can start a
SMTP debug server using this command:

    python -m smtpd -n -c DebuggingServer localhost:1025

Additionally set the SMTP port to 1025 in ``helfertool.yaml``:

The advantage of this method compared to the console backend from Django is,
that you also see the mails sent in Celery tasks in the same window.

# Code style

To run pylint and pep8 for all modules, run:

    ./scripts/check-codestyle.sh

The modules from `src/requirements_dev.txt` need to be installed for that.

The maximum line length is 120 characters, not 80.

# LICENSE

Copyright (C) 2019  Sven Hertle

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
