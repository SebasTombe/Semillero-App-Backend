#!/bin/bash
echo "Deteniendo aplicación en EC2..."
sudo systemctl stop gunicorn || true
