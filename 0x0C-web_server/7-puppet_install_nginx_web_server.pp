# configuration for nginx server

exec {'/usr/bin/env apt-get -y update':}

exec {'/usr/bin/env apt-get -y install nginx':}

exec {'/usr/bin/env echo "Hello World!" > /var/www/html/index.html':}

exec {'/usr/bin/env sed "/server_name _;/ a\ \\n\\tlocation /redirect_me {\\n\\trewrite ^/redirect_me(.*)$ https://www.grymoire.com/Unix/Sed.html permanent;\\n\\t}" -i /etc/nginx/sites-enabled/default':}

exec {'/usr/sbin/env nginx -t':}

exec {'/usr/sbin/env service nginx restart':}
