#configuration for header response

exec { 'HTTP response header':
	command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; sudo ufw --force enable; sudo ufw allow "Nginx HTTP"; sudo ufw allow 22; sudo sed -i "s/server_name _;/server_name roadsidedev.tech;\n\trewrite ^\/redirect_me https:\/\/youtube.com permanent;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default; sudo service nginx restart;',
	provider => shell,
}
