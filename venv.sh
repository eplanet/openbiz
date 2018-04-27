#!/bin/bash

AEROBIZ_VENV=~/.aerobiz

if [ ! -d $AEROBIZ_VENV ]
then
    virtualenv -p `which python3` $AEROBIZ_VENV
fi

source $AEROBIZ_VENV/bin/activate
pip install -r requirements.txt
