# Increase the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/bin:/bin/',
  notify  => Exec['nginx-restart'],  # Trigger the restart when the file is modified
}

# Ensure the file /etc/default/nginx exists
file { '/etc/default/nginx':
  ensure => present,
  # Add any specific content or attributes needed for the file, if required
}

# Restart Nginx
exec { 'nginx-restart':
  command     => 'service nginx restart',  # Use the appropriate command to restart Nginx
  path        => '/usr/sbin:/usr/bin:/sbin:/bin/',
  refreshonly => true,  # Only run this command if notified by other resources
  subscribe   => File['/etc/default/nginx'],  # Subscribe to changes in the nginx file
}
