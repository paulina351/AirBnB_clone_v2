<<<<<<< HEAD
ets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default
=======
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

>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee

service nginx restart
