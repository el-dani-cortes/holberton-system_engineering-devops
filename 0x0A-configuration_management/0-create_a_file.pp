file { '/tmp/holberton':
  ensure  => present, #the path of the new file
  owner   => 'www-data', #define owner of the file
  group   => 'www-data', #define group of the file
  mode    => '0744', #define permmission of the file
  content => 'I love Puppet', #content inside the file
  }
