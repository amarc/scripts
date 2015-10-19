#!/bin/bash

PKGS="apache2 apache2-bin apache2-data apache2-mpm-event apache2-suexec apache2-suexec-pristine libapache2-mod-fcgid php-pear php5-cgi php5-cli php5-common php5-curl php5-gd 
php5-imagick php5-json php5-mcrypt php5-mysql php5-readline php5-sqlite php5-xmlrpc php5-xsl mariadb-client mariadb-client-5.5 mariadb-client-core-5.5 mariadb-common mariadb-server 
mariadb-server-5.5 mariadb-server-core-5.5 bzip2 rsync dialog cron"

apt-get -y install $PKGS
