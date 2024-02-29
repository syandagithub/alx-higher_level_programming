#!/bin/bash
# It sends a request to an URL with curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
