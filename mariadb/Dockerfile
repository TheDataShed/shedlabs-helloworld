FROM centos:centos7

MAINTAINER Lewis Crawford <lewis@thedatashed.co.uk>

COPY mariadb.repo /etc/yum.repos.d/
RUN yum -y install --setopt=tsflags=nodocs mariadb-server mariadb && \ 
    yum -y update && yum clean all 
    
COPY docker-entrypoint.sh /entrypoint.sh
RUN chown mysql:mysql /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY mariadb-init.sh /mariadb-init.sh
CMD ["/bin/bash", "/mariadb-init.sh"]

USER mysql 
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 3306

CMD ["mysqld"]
