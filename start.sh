#!/bin/bash

python ./server.py & echo $!
python ./client.py & echo $!