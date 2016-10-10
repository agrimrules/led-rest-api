#!/bin/sh
docker run -d --privileged -v /dev/ttyUSB0:/dev/ttyUSB0 -v $(pwd):/app -p 5000:5000 agrimasthana/rpi-flask:delta
