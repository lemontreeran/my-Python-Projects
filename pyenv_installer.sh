sudo yum install curl git-core gcc make zlib-devel bzip2 bzip2-devel readline-devel sqlite \
sqlite-devel openssl-devel xz xz-devel libffi-devel

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
