#!/bin/bash
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
   export WORKON_HOME=$HOME/.virtualenvs 
   export PROJECT_HOME=$HOME/VENVPythonProj 
   export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
   source /usr/local/bin/virtualenvwrapper.sh
   #强制只允许在虚拟环境下安装软件
   #export PIP_REQUIRE_VIRTUALENV=true

   #alias virtualenvwrapper3='mkvirtualenv -p /usr/local/bin/python3.6' 
   #alias virtualenvwrapper2='mkvirtualenv -p /usr/bin/python2.7' 
   alias virtualenvwrapper3='mkvirtualenv ttenv --python=python3' 
   alias virtualenvwrapper2='mkvirtualenv ttenv --python=python2.7' 

   export PY2_HOME=/usr/bin/python2.7 
   export PY3_HOME=/usr/local/bin/python3
   alias v.mk2='mkvirtualenv -p $PY2_HOME'
   # alias v.mk3='mkvirtualenv -p $PY3_HOME'
   alias v.mk3='mkvirtualenv -p python3'
   alias v.rm='rmvirtualenv'
   alias v.switch='workon'
   alias v.add='add2virtualenv'
   alias v.setproj="setvirtualenvproject"
   alias v.proj2='mkproject -p $PY2_HOME'
   alias v.proj3='mkproject -p $PY3_HOME'
   alias v.cdproj='cdproject'
   alias v.cd='cdvirtualenv'
   alias v.cdsp='cdsitepackages'
   alias v.ls='lsvirtualenv'
   alias v.show='showvirtualenv'
   alias v.lssp='lssitepackages'
   alias v.exit='deactivate'
fi

