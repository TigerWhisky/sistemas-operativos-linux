#!/usr/bin/env bash
set -euo pipefail
echo "=== MOUNTS ==="; findmnt --real
echo "=== SPACE ==="; df -hT
echo "=== INODES ==="; df -ih
