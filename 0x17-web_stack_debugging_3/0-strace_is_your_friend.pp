#puppet manifest to rename a file and create a file

#exec {"mv class-wp-locale.php class-wp-locale.phpp":
	#command => "mv class-wp-locale.php class-wp-locale.phpp",
#        path => "/var/www/html/wp-includes"
#}

file {'/var/www/html/wp-includes/class-wp-locale.phpp':
	ensure => present,
        source => "/var/www/html/wp-includes/class-wp-locale.php",
}
