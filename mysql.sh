sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "CREATE USER 'dj@localhost' IDENTIFIED BY 'oOyE5K*3RGN$gjm{OTGA2{JZ7';"
mysql -uroot -e "GRANT ALL ON ask.* TO 'dj@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"