echo 'Delete container, delete volume and then bring back up..'
docker rm -f sqlimysql
docker volume prune -f
docker-compose up --build
