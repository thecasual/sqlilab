FROM mysql:5.7
ADD ./sql-dump /docker-entrypoint-initdb.d/
RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/