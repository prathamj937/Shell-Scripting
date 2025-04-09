#!/bin/bash

if [ "$EUID" -ne 0 ]; then
echo "Please run as a root"
exit 1
fi
read -p "Enter new username: " username
read -s -p "Enter Password: " password

useradd -m "$username"

echo "$username:$password" | chpasswd
echo "User '$username' created successfully"
