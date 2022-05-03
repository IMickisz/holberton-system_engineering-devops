# Automate the task of creating a custom HTTP header response (like in task 0), but with Puppet

exec { 'update':
command => '/usr/bin/apt-get update',
}

package { 'nginx':
ensure  => present,
name    => 'nginx',
require => Exec['update'],
}

file_line { 'Add header':
ensure  => 'present',
path    => '/etc/nginx/sites-available/default',
after   => 'server_name _;',
line    => 'add_header X-Served-By $hostname;',
require => Package['nginx'],
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
