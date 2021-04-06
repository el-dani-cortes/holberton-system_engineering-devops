# Practice configuring a server with Puppet! Just as you did before, 
# install and configure an Nginx server using Puppet instead of Bash. To save time and effort, include resources in 
# the manifest to perform a 301 redirect when querying /redirect_me.
include stdlib

# Install nginx package
exec { 'Update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
package { 'Nginx web server':
  name    => 'nginx',
}
->
# Create a file in /var/www/html with holberton school
file { 'Insert a string in index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => 'Holberton School',
}
->
# Edit a configuration file to redirect to another page
exec { 'Edit config nginx file to redirect to another page':
  command  => 'sed -i "42i \\\n\tlocation /redirect_me {\n\t\t return 301 https://www.youtube.com/watch?v=3MbaGJN2ioQ;\n\t}\n" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell',
}
->
# Restart web server
exec { 'Restart web server':
  command  => 'service nginx restart'
  user     => 'root',
  provider => 'shell',
}
