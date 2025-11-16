#!/bin/bash
echo "---"
free -h
echo "---"
top -b -n 1 | grep 'Mem:'
echo "---"
#df -h /dev/nvme0* | head -5
df -h /dev/nvme0* | head -5
iostat -x 5 1 | tail -5
