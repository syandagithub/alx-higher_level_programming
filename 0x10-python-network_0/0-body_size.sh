#!/bin/bash
# It sends a request to an URL with curl
curl -s "$1" | wc -c