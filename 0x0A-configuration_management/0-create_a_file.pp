# Puppet script to create a resource (file)

file { '/tmp/school':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0774',
  content => 'I love Puppet',
}
