#!/bin/bash
#bash script to get content length of a http response

curl -sI "$1" | awk '/Content-Length/ {print $2}'
