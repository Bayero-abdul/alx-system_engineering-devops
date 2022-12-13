# install flask from pip
exec {'install-flask':
  command => 'pip3 install flask==2.1.0',
  unless  => 'usr/bin/pip3 freeze | grep flask==2.1.0',
  path    => '.'
}
