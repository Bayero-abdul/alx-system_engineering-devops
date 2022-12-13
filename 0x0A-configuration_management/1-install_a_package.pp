# install flask from pip
exec {'install-flask':
  command => 'usr/bin/pip3 install flask==2.1.0',
  unless  => 'pip3 freeze | grep flask==2.1.0',
  path    => '.'
}
