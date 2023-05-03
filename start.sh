#!/bin/bash

python ./server.py & touch "server_pid_$!"
python ./client.py & touch "client_pid_$!"
