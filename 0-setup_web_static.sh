#!/usr/bin/env bash
# This script sets up a web server for the deployment of web_static.

# Update package list and install Nginx
apt-get update
apt-get install -y nginx

# Create directory structure for web_static
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a sample HTML file for testing
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link to the test release
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data/ to the ubuntu user and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure Nginx to serve web_static content
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME; # Add server name to HTTP headers
    root   /var/www/html; # Nginx document root
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current; # Serve web_static content
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/; # Redirect to cuberule.com
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html; # Serve custom 404 page
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx to apply changes
service nginx restart