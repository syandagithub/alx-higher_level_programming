#!/bin/bash
# This script takes in a URL as an argument and sends a GET request to the URL with a custom header
curl -s "$1" -X GET -H "X-School-User-Id: 98"
