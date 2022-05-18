#!/bin/bash

if [ ${UID} -ne 0 ]; then
    echo "[x] Must run as root !"
    exit 1
fi

# Configuration Manager
systemctl start gw_mp_config_manager
# MQTT Manager
systemctl start gw_mp_mqtt_manager