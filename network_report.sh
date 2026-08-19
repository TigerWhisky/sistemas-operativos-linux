#!/usr/bin/env bash
set -euo pipefail
echo "=== INTERFACES ==="; ip -br addr
echo "=== ROUTES ==="; ip route
echo "=== LISTENING SOCKETS ==="; ss -tuln
