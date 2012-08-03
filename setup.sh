#!/bin/sh

echo Copying files...
cp -r searchpy /usr/bin/
cp ser.py /usr/bin/serpy
echo Making serpy executable...
chmod +x /usr/bin/serpy
echo Complete! Type serpy for help
