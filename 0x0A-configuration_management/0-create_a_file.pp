file { '/tmp/school':
    ensure  => present,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0777',
    content => 'I love Puppet',
}
