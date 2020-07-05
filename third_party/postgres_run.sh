docker network create jdd_test
docker container kill postgres_jdd
docker container rm postgres_jdd
docker run --name postgres_jdd \
       --network jdd_test \
       -p 5432:5432 \
       -e POSTGRES_USER=postgres \
       -e POSTGRES_PASSWORD=mysecretpassword \
       -e POSTGRES_DB=jdd_test \
       -d postgres:12.0-alpine