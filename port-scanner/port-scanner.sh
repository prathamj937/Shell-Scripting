#!/bin/bash

HOST=$1
START_PORT=$2
END_PORT=$3

echo "🔍 Scanning $HOST from port $START_PORT to $END_PORT..."

for ((port=START_PORT; port<=END_PORT; port++)); do
    nc -zv -w 1 $HOST $port &> /dev/null
    if [ $? -eq 0 ]; then
        echo "🟢 Port $port is OPEN"
    else
        echo "🔴 Port $port is CLOSED"
    fi
done
