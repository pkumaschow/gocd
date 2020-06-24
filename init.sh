#!/bin/env bash

if [ -f "requirements.txt" ]; then
    if [ ! -d "venv" ]; then
        virtualenv --python=python2.7 venv
        echo active venv
        source venv/bin/activate
        # sudo apt-get install python-dev
        pip install --upgrade -r requirements.txt
    fi
fi

if [ -d "venv" ]; then
    source venv/bin/activate
fi

