#!/bin/bash

PKGS="apache2 apache2-bin apache2-data apache2-mpm-event apache2-suexec apache2-suexec-pristine libapache2-mod-fcgid php-pear php5-cgi php5-cli php5-common php5-curl php5-gd 
php5-imagick php5-json php5-mcrypt php5-mysql php5-readline php5-sqlite php5-xmlrpc php5-xsl mariadb-server bzip2 rsync dialog cron"


#MariaDB https://downloads.mariadb.org/mariadb/repositories

apt-get install software-properties-common
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
add-apt-repository 'deb http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu trusty main'

apt-get update && apt-get -y install $PKGS
