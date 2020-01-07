#!/bin/bash
#script that takes in a URL as an argument, sends a GET request to the URL
curl $1 -sX GET -H "X-HolbertonSchool-User-Id: 98"
