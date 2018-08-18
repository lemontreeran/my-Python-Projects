# python-virtualenv

First install pip for Python2. Download the get-pip.py file from https://bootstrap.pypa.io/get-pip.py
$ cd <download location>
$ sudo -H python ./get-pip.py

Installing pip also installs Python3
To run Python3
$ python3

Install pip3 by just executing the same file as in the step above, but this time using Python3
$ sudo -H python3 ./get-pip.py

To install virtualenv via pip
$ sudo -H pip3 install virtualenv

{If you want to use virtualenv as is, read below, else skip to the next pair of braces}

Note that virtualenv installs to the python3 directory. For me it's:
$ /usr/local/share/python3/virtualenv

Create a virtualenvs directory to store all virtual environments
$ mkdir somewhere/virtualenvs

Make a new virtual environment with no packages
$ virtualenv somewhere/virtualenvs/<project-name> --no-site-packages

To use the virtual environment
$ cd somewhere/virtualenvs/<project-name>/bin
$ source activate

You are now using the virtual environment for <project-name>. To stop:
$ deactivate

{Continue installation}

To install virtualenvwrapper
$ sudo -H pip3 install virtualenvwrapper

Use the following command to find the location of Python3 on your system
$ which python3

Add the following lines to ~/.bashrc (or your own shell's initialisation file)
> VIRTUALENVWRAPPER_PYTHON='<Python3 location>'
> source /usr/local/bin/virtualenvwrapper.sh
> export WORKON_HOME=$HOME/.virtualenvs

Run the following commands
$ mkdir ~/.virtualenvs
$ source ~/.bashrc

All the virtual environments created using virtualenvwrapper will now be stored in ./virtualenvs

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To create new Python3 virtual environment
$ mkvirtualenv <project name>

To create new Python2 virtual environment
$ mkvirtualenv --python=python2 <project name>

The virtualenv will automatically activate after creation

Install packages local to the python3 virtualenv (and not global to the system) using
$ pip3 install <package-name>

Install packages local to the python2 virtualenv (and not global to the system) using
$ pip install <package-name>

Activate a virtualenv:
$ workon <env name>

Install a package in the activated virtualenv
$ pip install <package name>

Go to its directory after activating it
$ cdvirtualenv

Set a working directory as a project of the virtualenv
$ cd <project dir>
$ setvirtualenvproject $VIRTUAL_ENV $(pwd)
If you have an existing code directory and want to attach it to a virtualenv to create a project then you use the setvirtualenvproject command:
$ setvirtualenvproject ~/.virtualenvs/newvirtualenv ~/workspace/existingcodedir

Get a list of the Python modules and versions installed in an activated virtualenv
$ pip freeze

To deactivate a virtualenv
$ deactivate

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To create a project you do:
$ mkproject <name of project>
This creates the virtual environment <name of project> in .virtualenvs, it also creates the project workspace ~/workspace/<name of project>.

When an environment is activated you can use the command cdproject to change to the top of the project working directory:
$ cdproject
If there is no -a when you do the mkvirtualenv, you have to manually create the .project file.
an example of setting the project path in your virtualenv
pwd > ~/.virtualenvs/<name of project>/.project

To work on a project you use the workon command. If there are no arguments it will list the available environments:
$ workon

To work in a specific sandbox environment you use workon with the name of the project:
$ workon virtenv1

To deactivate a sandbox and return to your standard environment:
$ deactivate

# Finally, to delete a specific project you use the rmvirtualenv command.


alias v="workon"
alias v.exit="deactivate"
alias v.ls="lsvirtualenv"
alias v.show="showvirtualenv"
alias v.init="mkvirtualenv"
alias v.rm="rmvirtualenv"
alias v.switch="workon"
alias v.add="add2virtualenv"
alias v.cd="cdproject"
alias v.cdsp="cdsitepackages"
alias v.cdenv="cdvirtualenv"
alias v.lssp="lssitepackages"
alias v.proj="mkproject"
alias v.setproj="setvirtualenvproject"
alias v.wipe="wipeenv"


alias v='workon'

alias v.mk='mkvirtualenv'
alias v.rm='rmvirtualenv'
alias v.switch='workon'
alias v.add='add2virtualenv'
alias v.setproj="setvirtualenvproject"
alias v.proj='mkproject'
alias v.cdproj='cdproject'
alias v.cd='cdvirtualenv'
alias v.cdsitepackages='cdsitepackages'
alias v.ls='lsvirtualenv'
alias v.show='showvirtualenv'
alias v.lssp='lssitepackages'
alias v.exit='deactivate'



