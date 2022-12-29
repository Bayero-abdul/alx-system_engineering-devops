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

file_line {'redirect':
  path    => '/etc/nginx/sites-enabled/default',
  after   => '^\tserver_name _;',
  line    => "\n\tlocation /redirect_me {\n\trewrite ^/redirect_me(.*)$ https://www.grymoire.com/Unix/Sed.html permanent;\n\t}",
  require =>  File['index.html'],
}

exec {'restart nginx':
  command =>  '/usr/sbin/service nginx restart',
  require =>  File_line['redirect'],
}
