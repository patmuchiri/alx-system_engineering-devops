# Puppet manifest to create the holberton user and adjust file limits

# Create the holberton user
user { 'holberton':
  ensure => present,
}

# Define limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton hard nofile 50000\nholberton soft nofile 50000",
}

# Set limits for the holberton user immediately
exec { 'apply-limits-holberton':
  command => '/bin/su - holberton -c "ulimit -n 50000"',
  path    => ['/bin', '/usr/bin'],
  require => User['holberton'],  # Ensure the user is created before setting limits
}
