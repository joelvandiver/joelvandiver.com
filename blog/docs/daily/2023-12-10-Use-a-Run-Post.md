---
title: Use a Run Script
date: 2023-12-10
description: Use a run script during development to streamline your development flow.
---

## Why `run`?

This `run` script was inspired by `npm run` scripts.  Moving your development flow to a run script allows you to setup environments, install, or anything else you need to develop your project.  The `run` script also allows your to consolidate your scripts into a single script.  You'd likely have an `install.sh` script, another for `test.sh`, etc.

## How to `run`?

### Add Current Directory to `$PATH`

To start, add the current directory to your `$PATH`.  I prefer to run scripts by name rather than with the relative path prefix (`./`).  So, I usually use `run` rather than `./run`.

```bash
# Add to `~/.bashrc`
export PATH="$PATH:."
```

### Add the Script

Setup a run script for quick development.

> Create the run script file:

```bash
$ touch run
```

> Add the run script:

```bash
#!/bin/bash

help() {
    echo "App"
    echo "========================="
    echo "start     Run the application"
    echo "test      Test the application"
}

# Setup Tab Complete
_tab_complete() {
    local cur prev opts
    opts="start test"
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

complete -F _tab_complete run

cmd=$1

# Remove the first argument (shift left)
shift

case $cmd in
    "start")
        echo "TODO: Add [start]"
        # Use "$@" to pass all remaining arguments.
        ;;
    "test")
        echo "TODO: Add [test]"
        # Use "$@" to pass all remaining arguments.
        ;;
    *)
        help
        ;;
esac
```

> Example run:

```bash
$ . run # Source the run script to add tab complete.
App
=========================
start     Run the application
test      Test the application
$ run start
TODO: Add [start]
```
