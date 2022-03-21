#configuration for header response

$str='frontend http_front
	bind *:80
	stats uri /haproxy?stats
	default_backend http_back
backend http_back
	balance roundrobin
	server 1919-web-01 34.148.87.245:80 check
	server 1919-web-02 3.231.218.82:80 check'
file_line {'/etc/haproxy/haproxy.cfg':
	ensure => present,
	path   => 'etc/haproxy/haproxy.cfg',
	line   => $str
}
