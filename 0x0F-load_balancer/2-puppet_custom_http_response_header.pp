# Custom HTTP header in a nginx server

# install nginx web server on server
package { 'nginx':
  ensure  => installed,
}

#  html web page that contains the string Holberton School
file { '/var/www/html/index.html':
  content => 'Holberton School',
}

# Add a redirection (/redirect_me) to another page
file_line { 'redirection site':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen [::]:80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=3MbaGJN2ioQ permanent;',
}

# custom 404 page that contains the string Ceci n'est pas une page.
file_line { 'custom 404 site':
  ensure => 'present',
  path   => '/var/www/html/custom_404.html',
  after  => '/server_name _;',
  line   => 'error_page 404 /custom_404.html;\n'
}

# custom Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}
# start service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}