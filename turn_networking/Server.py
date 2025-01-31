"""
Features:
Lobby Creation
Receive Action
Verify Action
Relay Action
Send Turn Permission
"""

import socket
import threading
import time

class Server:
	def __init__(self, ip="127.0.0.1", port=53849, timeout=1):
		self.ip = ip
		self.port = port

		self.connections = []
		self.rules = []

		self.timeout = timeout

		self.active = False
		self.response = None
		self.game_state_func = None

	# main loop
	def create_lobby(self, player_count): # Find a way to ensure that only the player_count can join
		self.active = True

		try:
			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as e: # add a throw
			print ("Socket creation failed: " + str(e))
			return
		try:
			server.bind((self.ip, self.port))
		except socket.error as e: # add a throw
			print ("Failed to bind socket: " + str(e))
			return

		server.settimeout(self.timeout)
		server.listen()

		while self.active:
			try:
				conn, addr = server.accept()
				self.connections.append(conn)
				client_thread = threading.Thread(target=self.handle_client, args=(addr, conn))
				client_thread.start()
			except socket.error as e: # add a throw
				pass

		server.close()
		client_thread.join()

	# Get the information return validity of received information
	def receive_action(self, conn):
		json = None
		# do timeout
		conn.settimeout(self.timeout)
		try:
			json = conn.recv(4096).decode("utf-8")
		except socket.timeout: # add throw
			pass
		except KeyboardInterrupt:
			conn.close()
		if (json != None):
			for rule in self.rules:
				if (self.verify_action(rule, json) == False):
					return False
			# make message
			self.make_game_state(json)
			return True
		return False

	# Rule will be a function that the json will be fed into
	def verify_action(self, rule, json):
		print (json)
		try:
			return rule(json)
		except Exception as e: # Definitly not how you are supposed to do it
			return False

	# send message to all connections
	def relay_action(self):
		if self.response == None:
			return
		for conn in self.connections:
			conn.send(self.response.encode("utf-8"))

	# Allow server shutdown
	def shutdown(self):
		self.active = False

	# Customize timeout
	def set_receive_timout(self, timeout):
		self.timeout = timeout

	# handle receive and relay of messages
	def handle_client(self, ip, conn):
		while self.active:
			#if (self.receive_action(conn) and self.response != None): # returns false if not recieved or invalid response
			#	self.relay_action() # tell all connections the move
			# 	self.reponse = None
			self.receive_action(conn)
			self.relay_action()

		self.connections.remove(conn)
		conn.close()

	# allow for custom rules to be added for verify_action()
	def add_rule(self, func):
		self.rules.append(func)

	def make_game_state(self, json):
		function = self.game_state_func
		self.response = function()

	def convert_game_state_func(self, func):
		self.game_state_func = func

	# Customize message to include lobby name? Or could just be user name of host
	def broadcast_lobby(self):
		# Port should a: be customizable, b: consitant across server instances
		broadcast_address = (self.ip, 5000)
		message = f"{self.ip}:{self.port}".encode("utf-8")

		broadcast_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		broadcast_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

		# Turn off after all players have joined?
		while self.active:
			broadcast_server.sendto(message, broadcast_address)
			time.sleep(5)
