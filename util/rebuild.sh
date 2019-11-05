echo 'Delete container, delete volume and then bring back up..'
#docker rm -f sql-lab1
#docker stop $(docker ps -a -q)
docker stop $(docker ps -f name=sql-lab -q)
docker rm $(docker ps -f name=sql-lab -a -q)
#docker volume prune -f
docker-compose up --build
