#puppet manifest to rename a file and create a file

exec {
	'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
	'touch /var/www/html/wp-content/db.php'
}
