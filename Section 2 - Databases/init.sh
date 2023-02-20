docker build -t my-postgres .
docker run -p 5432:5432 -d --name my-postgres my-postgres
docker start my-postgres 