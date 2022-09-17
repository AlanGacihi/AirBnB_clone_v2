#!/usr/bin/env bash
# This script sets up the servers.
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "If you can read this, it worked!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i '/^\tlocation \/ {$/i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
