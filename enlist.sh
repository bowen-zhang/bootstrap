#!/bin/bash

REPO=$1

cd $HOME/src
git clone http://github.com/bowen-zhang/$REPO

cd $HOME/src/$REPO

# Config GIT account
git config --global user.email bowenzhang1128@gmail.com
git config --global user.name "Bowen Zhang"
git config credential.helper store