#!/bin/bash
# script makes a request to 0.0.0.0:5000/catch_me
curl -s -L -X PUT -d "user_id=98" -H "You got me!" 0.0.0.0:5000/catch_me
