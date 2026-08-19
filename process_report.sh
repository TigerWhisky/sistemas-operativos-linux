#!/usr/bin/env bash
set -euo pipefail
echo "=== TOP PROCESSES ==="; ps -eo pid,ppid,user,stat,%cpu,%mem,comm --sort=-%cpu | head -n 20
echo "=== COUNT ==="; ps -e --no-headers | wc -l
echo "=== LOAD ==="; uptime
