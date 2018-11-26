#!/usr/bin/env bash

# NOTE: This file should be copied to /etc/profile.d/ directory
#       And all other files of this project should be copied to /etc/parental-control/ folder

# Debug message
echo "Running parental-control-login.sh!" >> ~/.config/parental-control/${USER}.log

# Configurations
PLC_DIR=/etc/parental-control

# Do parental control init
source ${PLC_DIR}/parental-control-init.sh

# Do parental control login functions in Python
python3 ${PLC_DIR}/parental-control.py "login" $PLC_CFG $USER $LOG_FIL

# Trap logout
EXITSCR=${PLC_DIR}/parental-control-logout.sh
trap 'source ${EXITSCR}' EXIT 0 1 2 3

