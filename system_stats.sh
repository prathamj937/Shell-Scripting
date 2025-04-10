#!/bin/bash

cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 +$4}')
mem_total=$(free -m | awk '/Mem:/ {print $2}')
mem_used=$(free -m | awk '/Mem:/ {print $3}')
disk=$(df -h / | awk 'NR==2 {print $5}')
uptime=$(uptime -p)

echo "{"
echo "  \"cpu\": \"$cpu\","
echo "  \"memory\": \"$mem_used / $mem_total MB\","
echo "  \"disk\": \"$disk\","
echo "  \"uptime\": \"$uptime\""
echo "}"
