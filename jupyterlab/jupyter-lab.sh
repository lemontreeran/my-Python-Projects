#!/bin/sh

# Based on:
# http://anbasile.github.io/programming/2017/06/25/jupyter-venv/

workspace=$1
mkvirtualenv --python=`which python3` ${workspace}
workon ${workspace}
pip3 install \
     jupyter jupyterlab jupyterthemes \
     scipy \
     numpy \
     pandas \
     matplotlib \
     seaborn \
     datarobot
pip3 install ipykernel
ipython kernel install --user --name=${workspace}-kernel

# Then run with:
#   jupyter lab
# or:
#   jupyter lab --core-mode
