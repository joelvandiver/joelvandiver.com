#!/bin/bash

# Add the root password.
sudo passwd root

# Add user joel.
adduser joel
usermod -aG sudo joel

# Log back in to debian as joel.
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl wget git vim

