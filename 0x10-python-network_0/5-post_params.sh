#!/bin/bash
# This script takes in a URLm and sends a POST request with specific parameters
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"

