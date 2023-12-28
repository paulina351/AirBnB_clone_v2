<<<<<<< HEAD
# Configures a web server for deployment of web_static.
=======
# Configures a web server to deploy web static
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
<<<<<<< HEAD

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

=======
    location /hbnb_static {
        alias /data/web_static/current;
        index indexhtml index.htm;
    }
    location /redirect_me {
        return 301 http://youtube.com/UCw4X_zayaSiuVYcqWpiaSWw;
    }
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data':
  ensure  => 'directory'
} ->

<<<<<<< HEAD
file { '/data/web_static':
  ensure => 'directory'
} ->

=======
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
file { '/data/web_static/releases':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

file { '/data/web_static/shared':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
<<<<<<< HEAD
  content => "Holberton School Puppet\n"
=======
  content => "Welcome to The_Masterminds home\n"
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
} ->

file { '/var/www/html':
  ensure => 'directory'
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
<<<<<<< HEAD
  content => "Holberton School Nginx\n"
=======
  content => "Welcome to The_Masterminds home\n"
>>>>>>> 5deed05b6952bc9554c76ee734006cbcef6542ee
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
