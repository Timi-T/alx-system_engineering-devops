# edit configuration file for ssh connections

$str = "IdentityFile ~/.ssh/school
        PasswordAuthentication no"
file { 'config':
  ensure  => 'present',
  path    => '/root/.ssh/config',
  content => $str,
}
