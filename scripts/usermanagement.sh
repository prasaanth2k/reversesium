#!/bin/sh
echo "[*] Creating user $1"
useradd -m $1
usermod -aG sudo $1
echo "$1:crackme@123" | chpasswd
sed -i "s|/bin/sh|/bin/bash|" /etc/passwd
echo "$1 ALL=(ALL) ALL" >> /etc/sudoers
cp /root/.bashrc /home/$1/.bashrc
echo "[*] $1 User added successfully"
