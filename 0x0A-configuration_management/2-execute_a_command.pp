# Create a manifest that kills a process named killmenow using Puppet
exec { 'kill process':
    command => 'pkill -f killmenow',
    path    => '/usr/bin',
}
