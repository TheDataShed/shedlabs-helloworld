#!/bin/bash
set -e

	DATADIR="/var/lib/mysql"
	
    	echo 'Running mysql_install_db ...'
		mysql_install_db --datadir="$DATADIR"
		echo 'Finished mysql_install_db'
		
		# These statements _must_ be on individual lines, and _must_ end with
		# semicolons (no line breaks or comments are permitted).
		# TODO proper SQL escaping on ALL the things D:
		
		tempSqlFile='/tmp/mysql-first-time.sql'
		cat > "$tempSqlFile" <<-EOSQL
			DELETE FROM mysql.user ;
			CREATE USER 'root'@'%' IDENTIFIED BY 'password' ;
			GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION ;
			DROP DATABASE IF EXISTS test ;
            CREATE DATABASE shed
		EOSQL
		
				
		echo 'FLUSH PRIVILEGES ;' >> "$tempSqlFile"
		
	
	
	chown -R mysql:mysql "$DATADIR"


mysqld --init-file="$tempSqlFile" &
mysql_pid=$!

until mysqladmin ping &>/dev/null; do
  echo -n "."; sleep 0.2
done

# Tell the MySQL daemon to shutdown.
mysqladmin --user=root --password=password shutdown

# Wait for the MySQL daemon to exit.
#wait $mysql_pid

# create a tar file with the database as it currently exists
#tar czvf default_mysql.tar.gz /var/lib/mysql

