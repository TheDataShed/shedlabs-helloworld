#!/bin/bash
set -e

if [ "${1:0:1}" = '-' ]; then
	set -- mysqld "$@"
fi

#Cannot use this method to set the passwd
#https://mariadb.atlassian.net/browse/MDEV-7656
#Leaving in for now until we get a better solution
if [ "$1" = 'mysqld' ]; then
	
	
	if [ ! -d "/tmp/change_passwd.sql" ]; then
		if [ -z "$MYSQL_ROOT_PASSWORD" -a -z "$MYSQL_ALLOW_EMPTY_PASSWORD" ]; then
			echo >&2 'error: database is uninitialized and MYSQL_ROOT_PASSWORD not set'
			echo >&2 '  Did you forget to add -e MYSQL_ROOT_PASSWORD=... ?'
			exit 1
		fi
		
		
		tempSqlFile='/tmp/change_passwd.sql'
		cat > "$tempSqlFile" <<-EOSQL
			
			SET PASSWORD FOR 'root'@'%' = PASSWORD('${MYSQL_ROOT_PASSWORD}') ;
			FLUSH PRIVILEGES;
			set global max_allowed_packet=67108864;
		EOSQL
		set -- "$@" --init-file="$tempSqlFile"
		
		
		
	fi
	
fi

exec "$@"