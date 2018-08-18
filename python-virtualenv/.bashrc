#!/bin/bash
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
   export WORKON_HOME=$HOME/.virtualenvs 
   export PROJECT_HOME=$HOME/VENVPythonProj 
   source /usr/local/bin/virtualenvwrapper.sh
   #强制只允许在虚拟环境下安装软件
   export PIP_REQUIRE_VIRTUALENV=true

   #alias virtualenvwrapper3='mkvirtualenv -p /usr/local/bin/python3.6' 
   #alias virtualenvwrapper2='mkvirtualenv -p /usr/local/bin/python2.7' 
   alias virtualenvwrapper3='mkvirtualenv ttenv --python=python3.6' 
   alias virtualenvwrapper2='mkvirtualenv ttenv --python=python2.7' 
fi
