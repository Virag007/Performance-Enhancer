#!/bin/sh

#Make sure docker is installed into your system and running
docker build -t petrack .
docker container run -it --name petrack petrack
