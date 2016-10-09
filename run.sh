#!/bin/sh
docker run -it --privileged -v /dev/ttyUSB0:/dev/ttyUSB0 -p 5000:5000 agrimasthana/rpi-flask:charlie
