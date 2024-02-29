#!/bin/bash
# It displays all HTTP methods that the server will when accept using curl.
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
