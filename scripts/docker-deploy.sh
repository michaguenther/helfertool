#!/bin/bash
if [ "$1" == "build" ] ; then
    docker build -t ikom/helfertool .
elif [ "$1" == "create" ] ; then
    docker run -d \
    --name ikomhelfertool \
    --restart always \
    -v "$PWD/mounts/data:/data" \
    -v "$PWD/mounts/config:/config" \
    -v "$PWD/mounts/log:/log" \
    -p 127.0.0.1:9000:8000 ikom/helfertool
elif [ "$1" == "start" ] ; then
    docker start ikomhelfertool
elif [ "$1" == "stop" ] ; then
    docker stop ikomhelfertool
elif [ "$1" == "rm" ] ; then
    docker container rm ikomhelfertool
else
    echo "commands: build, create, start, stop"
fi

