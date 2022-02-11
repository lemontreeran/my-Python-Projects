#!/bin/bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

alias pipup='pip install -U pip'

function pynew() {
    mkdir -p "$1" && cd "$1" &&  # passing `-p` means it doesn't fail if the dir exists
        pyenv virtualenv "$2" "$1"-"$2" &&  # create the new virtualenv
        pyenv local "$1"-"$2" &&  # set the new virtualenv to be the local Python version
        pipup &&  # a bash alias for pip install --upgrade pip
        pip install pylint &&  # for Python linting in Sublime Text
        [ -e "requirements.txt" ] &&  # check if requirements.txt exists...
        pip install -r requirements.txt  # ...and if it does, install it
}

