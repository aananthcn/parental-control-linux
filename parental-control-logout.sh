#!/usr/bin/env bash

# NOTE: This file should be copied to /etc/parental-control directory

# Debug message
echo "Running parental-control-logout.sh" >> ~/.config/parental-control/${USER}.log

# Configurations
PLC_DIR=/etc/parental-control

# Do parental control init
source ${PLC_DIR}/parental-control-init.sh

# Do parental control login functions in Python
python3 ${PLC_DIR}/parental-control.py "logout" $PLC_CFG $USER $LOG_FIL


