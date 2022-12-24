# configuration for nginx server

exec {'/usr/bin/env apt-get update':}

exec {'/usr/bin/env apt-get -y install nginx':}

exec {'/usr/bin/env echo "Hello World!" > /var/www/html/index.html':}

$location='\n\tlocation /redirect_me {\n\trewrite ^/redirect_me(.*)$ https://www.grymoire.com/Unix/Sed.html permanent;\n\t}'

exec { "/usr/bin/env sed '/server_name _;/ a\ ${location}' -i /etc/nginx/sites-enabled/default":}

exec {'/usr/bin/env sed -i "/server_name _;/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-enabled/default':}

exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html':}

exec {'/usr/bin/env service nginx restart':}
