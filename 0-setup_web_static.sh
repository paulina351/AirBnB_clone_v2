#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment

sudo apt update
sudo apt install nginx

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/current/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>

ln -s /data/web_static/releases/test/ /data/web_static/current

chown -r /data/ ubuntu


service nginx restart
