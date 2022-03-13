# edit configuration file for ssh connections

file_line { 'disable password login':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'declare identity file':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
