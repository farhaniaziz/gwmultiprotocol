#!/bin/bash

GW_MP_CONFDIR="/etc/gwmp"
GW_MP_DESTDIR="/opt/gwmp"
GW_MP_SYSTEMD="/etc/systemd/system"

# Install project in the system
do_install(){
    cp config/config.json ${GW_MP_CONFDIR}
    cp -r utils ${GW_MP_DESTDIR}
    cp *.py ${GW_MP_DESTDIR}
    cp systemd/*.service ${GW_MP_SYSTEMD}
    systemctl daemon-reload
    echo "[*] Project files are installed."
}

do_preinstall(){
    if ! test -d ${GW_MP_CONFDIR}; then
        mkdir ${GW_MP_CONFDIR}
    fi

    if ! test -d ${GW_MP_DESTDIR}; then
        mkdir ${GW_MP_DESTDIR}
    fi

    pip3 install -r requirements.txt
    echo "[*] Project dependencies are installed."
}

# Check if user is root
if [ ${UID} -ne 0 ]; then
    echo "[x] Must run as root."
    exit 1
fi

do_preinstall
do_install
echo "[*] Project is installed."