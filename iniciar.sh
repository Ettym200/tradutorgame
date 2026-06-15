#!/bin/bash
cd "$(dirname "$0")"
pip install -r requirements.txt -q

if [ "$EUID" -ne 0 ]; then
    echo "Solicitando permissão para hotkeys globais..."
    sudo python3 main.py
else
    python3 main.py
fi
