# configuration for nginx server

include stdlib

exec {'update file':
  command => '/usr/bin/env apt-get -y update',
  before  =>  Exec['install nginx'],
}

exec {'install nginx':
  command =>  '/usr/bin/env apt-get -y install nginx',
  require => Exec['update file'],
}

file {'index.html':
  ensure  => present,
  path    =>  '/var/www/html/index.html',
  content => "Hello World!\n",
  require => Exec['install nginx'],
}

file {'custom_404.html':
  ensure  => present,
  path    => '/var/www/html/custom_404.html',
  content => "Ceci n'est pas une page\n",
  require => File['index.html'],
}

file_line {'redirect':
  path    => '/etc/nginx/sites-enabled/default',
  after   => '^\tserver_name _;',
  line    => "\n\tlocation /redirect_me {\n\trewrite ^/redirect_me(.*)$ https://www.grymoire.com/Unix/Sed.html permanent;\n\t}",
  require =>  File['custom_404.html'],
}

file_line {'error_404':
  path    => '/etc/nginx/sites-enabled/default',
  after   => '^\tserver_name _;',
  line    => "\n\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}",
  require => File_line['redirect'],
}

file_line {'header':
  path    => '/etc/nginx/sites-enabled/default',
  after   => '^\tserver_name _;',
  line    => "\n\tadd_header X-Served-By \$HOSTNAME;",
  require => File_line['error_404'],
}

exec {'restart nginx':
  command =>  '/usr/sbin/service nginx restart',
  require =>  File_line['header'],
}
