# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message

exec {'add holberton user':
path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
command => 'sed -i "s/holberton/#holberton/" /etc/security/limits.conf',
}
