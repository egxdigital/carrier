#!/bin/bash
#
# Re-install the Python program after installing a new dependency.
#
# USAGE: 
#    Ensure that your user is the owner of the project root before executing this script.
#    Use command: sudo chown -R user:user /path/to/project/root
#    Do not run the script as superuser
#    Do not change the lines in the script to run a ssuperuser
# RUN:
#    ./install.sh

source env/bin/activate
pip freeze > requirements.txt
python3.10 -m build
deactivate
python3.10 -m pip install --editable .