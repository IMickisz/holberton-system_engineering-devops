# Update the limit of open files

exec {'update limit':
path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
command => 'sed -i s/15/2000/ /etc/default/nginx',
}

exec {'restart nginx':
path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
command => 'sudo service nginx restart',
}
