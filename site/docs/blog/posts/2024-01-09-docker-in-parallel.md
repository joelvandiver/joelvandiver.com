---
title: Parallelized Docker Builds
date: 2024-01-09
description: Docker supports parallelized, multistage builds.
---

# Parallelized Docker Builds

## Serial Builds

When creating a `Dockerfile`, we may be able to split up our work into multiple stages to distribute the work in parallel.  To simulate a large build, let's setup a `Dockerfile` with 3 `sleep 5` tasks in a single-stage build.

```Dockerfile
FROM debian:12.4
WORKDIR /app
RUN sleep 5 && echo "task1 Done" > /app/task1.log
RUN sleep 5 && echo "task2 Done" > /app/task2.log
RUN sleep 5 && echo "task3 Done" > /app/task3.log
```

```bash
time DOCKER_BUILDKIT=1 docker build --tag serial_test .
```
```log
[+] Building 23.2s (12/12) FINISHED                                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 288B                                                                                      0.0s
 => [internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [internal] load metadata for docker.io/library/debian:12.4                                                            1.0s
 => [1/8] FROM docker.io/library/debian:12.4@sha256:bac353db4cc04bc672b14029964e686cd7bad56fe34b51f432c1a1304b9928da      4.1s
 => => resolve docker.io/library/debian:12.4@sha256:bac353db4cc04bc672b14029964e686cd7bad56fe34b51f432c1a1304b9928da      0.0s
 => => sha256:bac353db4cc04bc672b14029964e686cd7bad56fe34b51f432c1a1304b9928da 1.85kB / 1.85kB                            0.0s
 => => sha256:0dc902c61cb495db4630a6dc2fa14cd45bd9f8515f27fbb12e3d73a119d30bf1 529B / 529B                                0.0s
 => => sha256:2a033a8c63712da54b5a516f5d69d41606cfb5c4ce9aa1690ee55fc4f9babb92 1.46kB / 1.46kB                            0.0s
 => => sha256:bc0734b949dcdcabe5bfdf0c8b9f44491e0fce04cb10c9c6e76282b9f6abdf01 49.56MB / 49.56MB                          2.2s
 => => extracting sha256:bc0734b949dcdcabe5bfdf0c8b9f44491e0fce04cb10c9c6e76282b9f6abdf01                                 1.7s
 => [2/8] WORKDIR /app                                                                                                    0.2s
 => [3/8] RUN sleep 5 && echo "task1 Done" > /app/task1.log                                                               5.3s
 => [4/8] RUN sleep 5 && echo "task2 Done" > /app/task2.log                                                               5.4s
 => [5/8] RUN sleep 5 && echo "task3 Done" > /app/task3.log                                                               5.5s
 => [6/8] RUN cat /app/task1.log                                                                                          0.4s
 => [7/8] RUN cat /app/task2.log                                                                                          0.6s
 => [8/8] RUN cat /app/task3.log                                                                                          0.5s
 => exporting to image                                                                                                    0.2s
 => => exporting layers                                                                                                   0.1s
 => => writing image sha256:5a4ba49cbde2f6178268ca9d428fc6e0a831cdbaecb1a13a92730d473d21990a                              0.0s
 => => naming to docker.io/library/serial_test                                                                            0.0s

What's Next?
  1. Sign in to your Docker account → docker login
  2. View a summary of image vulnerabilities and recommendations → docker scout quickview

real    0m23.594s
user    0m0.133s
sys     0m0.141s
```

> The serial build ran in 23.6 secs.

## Parallel Builds

Did you realize that Docker supports building stages in parallel?  This can greatly reduce build times depending on the service being built.  For example, let's take the following Dockerfile:

```Dockerfile
FROM debian:12.4 as task1
WORKDIR /app
RUN sleep 5 && echo "task1 Done" > /app/result.log

FROM debian:12.4 as task2
WORKDIR /app
RUN sleep 5 && echo "task2 Done" > /app/result.log

FROM debian:12.4 as task3
WORKDIR /app
RUN sleep 5 && echo "task3 Done" > /app/result.log

FROM debian:12.4 as Final

WORKDIR /app
COPY --from=task1 /app/result.log /app/task1.log
COPY --from=task2 /app/result.log /app/task2.log
COPY --from=task3 /app/result.log /app/task3.log
```

```bash
time DOCKER_BUILDKIT=1 docker build --tag parallel_test .
```
```log
[+] Building 11.3s (12/12) FINISHED                                                                                           docker:default
 => [internal] load build definition from Dockerfile                                                                          0.0s
 => => transferring dockerfile: 510B                                                                                          0.0s
 => [internal] load .dockerignore                                                                                             0.0s
 => => transferring context: 2B                                                                                               0.0s
 => [internal] load metadata for docker.io/library/debian:12.4                                                                1.0s
 => [stage3 1/3] FROM docker.io/library/debian:12.4@sha256:bac353db4cc04bc672b14029964e686cd7bad56fe34b51f432c1a1304b9928da   4.0s
 => => resolve docker.io/library/debian:12.4@sha256:bac353db4cc04bc672b14029964e686cd7bad56fe34b51f432c1a1304b9928da          0.0s
 => => sha256:bac353db4cc04bc672b14029964e686cd7bad56fe34b51f432c1a1304b9928da 1.85kB / 1.85kB                                0.0s
 => => sha256:0dc902c61cb495db4630a6dc2fa14cd45bd9f8515f27fbb12e3d73a119d30bf1 529B / 529B                                    0.0s
 => => sha256:2a033a8c63712da54b5a516f5d69d41606cfb5c4ce9aa1690ee55fc4f9babb92 1.46kB / 1.46kB                                0.0s
 => => sha256:bc0734b949dcdcabe5bfdf0c8b9f44491e0fce04cb10c9c6e76282b9f6abdf01 49.56MB / 49.56MB                              2.1s
 => => extracting sha256:bc0734b949dcdcabe5bfdf0c8b9f44491e0fce04cb10c9c6e76282b9f6abdf01                                     1.7s
 => [stage3 2/3] WORKDIR /app                                                                                                 0.1s
 => [stage2 3/3] RUN sleep 5 && echo "stage2 Done" > /app/result.log                                                          5.4s
 => [stage1 3/3] RUN sleep 5 && echo "stage1 Done" > /app/result.log                                                          5.7s
 => [stage3 3/3] RUN sleep 5 && echo "stage3 Done" > /app/result.log                                                          5.7s
 => [final 3/5] COPY --from=stage1 /app/result.log /app/stage1.log                                                            0.0s
 => [final 4/5] COPY --from=stage2 /app/result.log /app/stage2.log                                                            0.0s
 => [final 5/5] COPY --from=stage3 /app/result.log /app/stage3.log                                                            0.0s
 => exporting to image                                                                                                        0.1s
 => => exporting layers                                                                                                       0.1s
 => => writing image sha256:9a00f8d862f8f76d2fdebcafa1128c4be35aea5088804c431dc44101907ccb8e                                  0.0s
 => => naming to docker.io/library/parallel_test                                                                              0.0s

What's Next?
  1. Sign in to your Docker account → docker login
  2. View a summary of image vulnerabilities and recommendations → docker scout quickview

real    0m11.607s
user    0m0.060s
sys     0m0.176s
```

> The parallel build ran in 11.6 secs.

Very cool!

## Notes

I was surprised to find this `Dockerfile` does not run the first and second stages if they're not used in the final stage:

```Dockerfile
FROM debian:12.4 as task1
WORKDIR /app
RUN sleep 5 && echo "task1 Done" > /app/result.log

FROM debian:12.4 as task2
WORKDIR /app
RUN sleep 5 && echo "task2 Done" > /app/result.log

FROM debian:12.4 as task3
WORKDIR /app
RUN sleep 5 && echo "task3 Done" > /app/result.log
```

Docker detects that the `task1` and `task2` stages are not used in the `task3` stage (through a `COPY --from=...`), so it skips them!

```bash
time DOCKER_BUILDKIT=1 docker build --tag skip_test .
```
```log
[+] Building 6.2s (7/7) FINISHED                                                                                             docker:default
 => [internal] load .dockerignore                                                                                            0.0s
 => => transferring context: 2B                                                                                              0.0s
 => [internal] load build definition from Dockerfile                                                                         0.0s
 => => transferring dockerfile: 310B                                                                                         0.0s
 => [internal] load metadata for docker.io/library/debian:12.4                                                               0.8s
 => [task3 1/3] FROM docker.io/library/debian:12.4@sha256:bac353db4cc04bc672b14029964e686cd7bad56fe34b51f432c1a1304b9928da   0.0s
 => CACHED [task3 2/3] WORKDIR /app                                                                                          0.0s
 => [task3 3/3] RUN sleep 5 && echo "task3 Done" > /app/result.log                                                           5.3s
 => exporting to image                                                                                                       0.0s
 => => exporting layers                                                                                                      0.0s
 => => writing image sha256:965ebe3258d6e1fb724b1130164dfdaae7ad2fef048f3fd21afcb8b9f9178f73                                 0.0s
 => => naming to docker.io/library/skip_test                                                                                 0.0s

What's Next?
  1. Sign in to your Docker account → docker login
  2. View a summary of image vulnerabilities and recommendations → docker scout quickview

real    0m6.584s
user    0m0.066s
sys     0m0.162s
```

> Note the missing `task1` and `task2` stages in the output above.

## References

- [Multi-stage | Docker Docs](https://docs.docker.com/build/guide/multi-stage/#parallelism)