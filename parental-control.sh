#!/usr/bin/env bash

# NOTE: This file should be copied to /etc/profile.d/ directory
#       And all other files of this project should be copied to /etc/parental-control/ folder


# Configurations
PLC_DIR=/etc/parental-control
PLC_CFG=${PLC_DIR}/parental-control.cfg
LOG_DIR=~/.config/parental-control
LOG_FIL=${LOG_DIR}/${USER}.log

# Log file handling
mkdir -p ${LOG_DIR}
touch ${LOG_FIL}

# Debug message
echo "Running parental-control.sh!" >> ~/.config/parental-control/${USER}.log

# Configuration file handling
if [[ -r ${PLC_CFG} ]]
    then
        # Check if Python is installed
        if command -v python3 &>/dev/null; then
            python3 --version
        else
            echo "*** Error ***: Python 3 is not installed, please install" >> ~/.config/parental-control/${USER}.log
            exit -1
        fi
else
    echo "${PLC_CFG} not found! Please run install script!" >> ~/.config/parental-control/${USER}.log
    exit -1
fi

# Do parental control login functions in Python
python3 ${PLC_DIR}/parental-control.py $PLC_CFG $USER $LOG_FIL

