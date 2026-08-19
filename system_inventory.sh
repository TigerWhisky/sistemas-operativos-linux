#!/usr/bin/env bash
set -euo pipefail
echo "=== SYSTEM ==="; uname -a
echo "=== OS ==="; cat /etc/os-release 2>/dev/null || true
echo "=== CPU ==="; nproc; lscpu | sed -n '1,18p'
echo "=== MEMORY ==="; free -h
echo "=== FILESYSTEMS ==="; df -hT
