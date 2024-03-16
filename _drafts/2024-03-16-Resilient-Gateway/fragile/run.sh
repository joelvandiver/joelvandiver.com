#!/bin/bash

docker run --rm -p 80:80 -v $PWD/nginx.conf:/etc/nginx/nginx.conf --name gateway nginx:latest