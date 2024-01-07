#!/bin/bash

sudo apt install g++
sudo apt-get update -y && sudo apt-get install build-essential curl libffi-dev libffi7 libgmp-dev libgmp10 libncurses-dev libncurses5 libtinfo5 -y


# ref: https://www.haskell.org/ghcup/install/
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh