# edit configuration file for ssh connections

$str = "Host 35.231.246.241
	Hostname 35.231.246.241
	IdentityFile	~/.ssh/school
	PasswordAuthentication no"
file { 'config':
  ensure  => 'present',
  path    => '/root/.ssh/config',
  content => $str,
}
