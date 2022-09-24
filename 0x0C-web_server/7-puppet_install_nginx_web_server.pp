#! Setup nginx server

package { 'nginx':
  ensure  => 'installed'
}

file { 'Hello World':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World'
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com permanent;'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
