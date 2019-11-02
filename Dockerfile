FROM mysql:5.7
ADD ./mysql-dump /docker-entrypoint-initdb.d/
RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/