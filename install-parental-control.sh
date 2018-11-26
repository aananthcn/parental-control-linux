#!/usr/bin/env bash

# Configurations
PLC_DIR=/etc/parental-control

# Install init script
sudo install -o root ./parental-control-login.sh /etc/profile.d/

# Install core and logout scripts
sudo mkdir -p ${PLC_DIR}
sudo install -o root ./parental-control* ${PLC_DIR}/
