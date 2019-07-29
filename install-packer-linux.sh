#!/bin/bash -e

workdir=/tmp/packer
pversion=0.10.1

which packer || {
  mkdir -p $workdir
  cd $workdir
  sudo yum install unzip wget
  wget https://releases.hashicorp.com/packer/$pversion/packer_${pversion}_linux_amd64.zip && \
  unzip packer_${pversion}_linux_amd64.zip && \
  mv packer /usr/local/bin/
  rm -Rf $workdir
  
  packer -v
}
echo "Go ahead and enjoy packer"
