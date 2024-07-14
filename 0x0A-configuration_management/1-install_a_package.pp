#!/usr/bin/pup
# This Puppet Manifest installs Flask using pip3


package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

exec { 'werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
}

