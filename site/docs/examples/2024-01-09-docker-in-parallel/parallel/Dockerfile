FROM debian:12.4 as stage1
WORKDIR /app
RUN sleep 5 && echo "stage1 Done" > /app/result.log

FROM debian:12.4 as stage2
WORKDIR /app
RUN sleep 5 && echo "stage2 Done" > /app/result.log

FROM debian:12.4 as stage3
WORKDIR /app
RUN sleep 5 && echo "stage3 Done" > /app/result.log

FROM debian:12.4 as Final

WORKDIR /app
COPY --from=stage1 /app/result.log /app/stage1.log
COPY --from=stage2 /app/result.log /app/stage2.log
COPY --from=stage3 /app/result.log /app/stage3.log