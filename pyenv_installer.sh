#!/bin/bash
# https://github.com/pyenv/pyenv/wiki#suggested-build-environment
# Ubuntu/Debian/Mint:
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
# CentOS/Fedora 21 and below:
yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel
# Fedora 22 and above
dnf install make gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel

if [ ! -d "$HOME/.pyenv" ]; then
  echo "===== Installing pyenv ====="
  curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
fi
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

BASH_PROFILE="$HOME/.bashrc"

if [[ ! $(cat $BASH_PROFILE | grep "pyenv init") ]]; then
  echo "Set the $BASH_PROFILE for pyenv"
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $BASH_PROFILE
  echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> $BASH_PROFILE
  echo 'eval "$(pyenv init -)"' >> $BASH_PROFILE
  echo 'eval "$(pyenv virtualenv-init -)"' >> $BASH_PROFILE
fi

echo "Initialize pyenv environment..."
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
