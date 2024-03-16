#!/bin/bash

docker run --rm -p 80:80 -v $PWD/nginx.conf:/etc/nginx/nginx.conf --name gateway nginx:latest

cd flaky
docker build -t flaky .
docker run --rm -p 8000:8000 --name flaky --network resilient-nw flaky
