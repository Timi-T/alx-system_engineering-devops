#puppet manifest to rename a file and create a file

exec {"/var/www/html/wp-includes/class-wp-locale.php":
	command => "mv class-wp-locale.php class-wp-locale.phpp",
        path => "/var/www/html/wp-includes"
}
