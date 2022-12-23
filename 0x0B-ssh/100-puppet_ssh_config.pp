include stdlib

$filename = '/etc/ssh/ssh_config'

#conigure the password authentication to no
file_line {'passwd_auth':
  path  => $filename,
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
}


# configure the identity file
file_line {'identity_file':
  path  => $filename,
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}
