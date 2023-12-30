---
layout: post
title: Git Flow Simplified
date: 2021-12-03
description: My git flow has evolved yet again!
---

Oh, there are so many ways of managing git repositories.  I've written on this topic before, but as usual, things have changed.  I recently changed teams at work, and with a new team comes a new culture of devops.  

## TL;DR

> "CI" means to continuously integrate, so sync often.

## Simple Git Flow

1. Keep to a single trunk (such as `/develop`)
2. Commit on *all* logically complete units of code.
3. Fetch from remote.
4. Rebase.
5. Push.
6. Repeat > 5x/day

I usually script the above like this:

> sync.sh

```sh
#!/bin/sh
message=$1
git add -A
git commit -m "${message}"
git fetch
git rebase
git push
```

## CI vs Branching

By definition "continuous integration" and "branching" are antithetical to each other.  I used to think of "CI" as something the server does to integrate developers code.  But, I now see that the developers' systems are also a point of integration.  

The goal is to integrate as quickly as possible (hence "continuous").  

## Still Branch?

Ok, ok, I have to be pragmatic and say that I still branch.  I now use branching for experimental coding, prototyping, and just figuring things out.  But I try to get off the branch within a couple of hours.  

Quite frankily, if I knew everything about all code that I'll ever need to write, *then* I would avoid branching completely.  

So, for branching, I usually script it such as this:

> branch.sh

```sh
#!/bin/sh
branch=$1
git checkout -b $branch
git push -u origin $branch
```

Then, when I'm ready to merge back to trunk (`/develop`) I complete my branch:

> complete.sh

```sh
#!/bin/sh
message=$1
git add -A
git commit -m "${message}"
git push
current_branch=$(git branch --show-current)
git checkout develop
git merge --squash $current_branch
git commit -m "${message}"
git push $1
git branch -d $current_branch
git push origin --delete $current_branch
```

**Note:** I use `git merge --squash $current_branch` to keep the commits on trunk (`/develop`) clean.