---
layout: post
title: Dockerize Your Development Today!
date: 2023-06-15
description: Dockerize your development environment.
---

## No More "It Works on My Machine" Excuses

We've all been there. Code that works on my machine doesn't work on yours and vice versa. But, why?  There are like a number of issues to troubleshoot.  Some of the most common are:

1. Different versions of the programming language, sdk, and runtime.
2. Different package versions.
3. Different operating systems.
4. Different software toolchains.
5. ...

The list goes on and on.

## Docker to the Rescue

Docker is great for containerizing your services in production.  But, we can do better.  Why not use it to containerize your development environment?  This way, you can be sure that your development environment matches your production environment exactly.  No more surprises, no more excuses.

You can simply build a new image when anything on the list above changes and push it to shared container registry for the team.  Then, you can check in the image tag to version control and everyone can spin up an identical environment in minutes.  No more wasted time setting up dependencies and configuring tools.

Check out vscode's [dev containers](https://code.visualstudio.com/docs/remote/containers) for more information.

Once I started using docker for development, I never looked back.  It's a game changer.