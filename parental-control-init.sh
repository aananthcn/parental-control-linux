#!/usr/bin/env bash

# NOTE: This file should be copied to /etc/parental-control directory

echo "Running parental-control-init.sh!" >> ~/.config/parental-control/${USER}.log
PLC_CFG=${PLC_DIR}/parental-control.cfg
LOG_DIR=~/.config/parental-control
LOG_FIL=${LOG_DIR}/${USER}.log

# Log file handling
mkdir -p ${LOG_DIR}
touch ${LOG_FIL}

# Configuration file handling
if [[ -r ${PLC_CFG} ]]
    then
        echo "Opening ${PLC_CFG}!"
        # Check if Python is installed
        if command -v python3 &>/dev/null; then
            python3 --version
        else
            echo "*** Error ***: Python 3 is not installed, please install" >> ~/.config/parental-control/${USER}.log
            exit -1
        fi
else
    echo "${PLC_CFG} not found!" >> ~/.config/parental-control/${USER}.log
    exit -1
fi


