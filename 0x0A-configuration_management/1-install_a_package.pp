# install flask from pip
exec {'install-flask':
  command => '/bin/pip3 install flask==2.1.0',
  path    => '.'
}
