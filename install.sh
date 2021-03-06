#!/bin/bash

sudo sudo apt-get install python3-setuptools
sudo easy_install3 pip

cat <<eof > in
PyYAML==3.11
arrow==0.6.0
base58==0.2.2
docker-py==1.8.0
flake8==2.5.4
future==0.15.2
jsonrpcclient==2.0.1
jsonrpcserver==3.1.1
mccabe==0.4.0
mnemonic==0.13
mock==1.3.0
path.py==7.7.1
pbkdf2==1.3
pep8==1.7.0
pexpect==4.0.1
protobuf==3.0.0a3
pyaes==1.3.0
pyflakes==1.0.0
pytest==2.9.1
requests==2.7.0
responses==0.5.0
sha256==0.1
simplejson==3.7.3
tabulate==0.7.5
eof

sudo pip3 install -r in
     
rm -f in

echo '"./txHex2JSON" to run'
