FROM debian:12.4 as task1
WORKDIR /app
RUN sleep 5 && echo "task1 Done" > /app/result.log

FROM debian:12.4 as task2
WORKDIR /app
RUN sleep 5 && echo "task2 Done" > /app/result.log

FROM debian:12.4 as task3
WORKDIR /app
RUN sleep 5 && echo "task3 Done" > /app/result.log