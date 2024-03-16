---
title: Resilient Gateway
date: 2024-03-16
description: Define a resilient nginx application gateway.
categories:
    - Microservices
    - Cloud
---

Out of the box, Nginx requires all backend services to be available before it comes up.

## Fragile Gateway

First up, let's add a docker network to add the gateway and backend service to later.

```bash
docker network create resilient-nw
```

Let's add a simple `nginx.conf` that requires a backend service named `flaky`.

```conf
events {
    worker_connections 1024;
}

http {
    server {
        listen 80;

        location /flaky {
            proxy_pass http://flaky:8000;
        }
    }
}
```

Let's startup nginx without the flaky service:

```bash
docker run --rm -p 80:80 --network resilient-nw -v $PWD/nginx.conf:/etc/nginx/nginx.conf --name gateway nginx:latest
```

Note that nginx won't come up when the flaky service isn't up:

```log
...
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/03/16 22:10:30 [emerg] 1#1: host not found in upstream "flaky" in /etc/nginx/nginx.conf:6
nginx: [emerg] host not found in upstream "flaky" in /etc/nginx/nginx.conf:6
```

In my opinion, this scenario should have been handled by Nginx.  But, get around this, we can set the proxied backend to a variable.

## Resilient Gateway

Now, let's setup a resilient gateway.

```conf
events {
    worker_connections 1024;
}

http {
    server {
        listen 80;

        set $flaky "http://flaky:8000";
        
        location /flaky {
            proxy_pass $flaky;
        }
    }
}
```

Let's fire up the gateway again:

```bash
docker run --rm -p 80:80 --network resilient-nw -v $PWD/nginx.conf:/etc/nginx/nginx.conf --name gateway nginx:latest
```

Now, the gateway comes up without a problem.  But what happens when we try to get the `/flaky` path?

```bash
curl http://localhost/flaky/
<html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
<hr><center>nginx/1.25.4</center>
</body>
</html>
```

That's interesting!  Now, we're getting the `502 Bad Gateway` as expected!

Let's confirm, though, that gateway can call the flaky service after the flaky service is up and running.

### Flaky Service

I'll try to keep this simple, so I'll create a running docker container of an expressjs app.

> `server.js`

```javascript
const express = require('express');
const app = express();
const port = 8000;

app.get('/flaky', (req, res) => {
  res.send("I'm here.");
});

app.listen(port, () => {
  console.log(`Flaky service listening at http://localhost:${port}`);
});
```

> `package.json`

```json
{
  "name": "flaky",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.3"
  }
}
```

> `Dockerfile`

```Dockerfile
FROM node:20
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 8000
CMD ["npm", "start"]
```

```bash
cd flaky
docker build -t flaky .
...
docker run --rm -p 8000:8000 --name flaky --network resilient-nw flaky
> flaky@1.0.0 start
> node server.js

Flaky service listening at http://localhost:8000
```

Hmmm, now I'm still getting a `502 Bad Gateway`!

```bash
172.18.0.1 - - [16/Mar/2024:22:38:46 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost/flaky" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
```

We need a dns resolver for Nginx to dynamically lookup the backend service.

```conf
resolver 127.0.11 valid=30s;  # Docker's internal DNS server.
```

