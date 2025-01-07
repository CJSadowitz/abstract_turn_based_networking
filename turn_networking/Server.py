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

class Server:
	def __init__(self, ip="127.0.0.1", port=53849, timeout=0.1):
		self.ip = ip
		self.port = port

		self.connections = []
		self.rules = []

		self.timeout = timeout

		self.active = False
		self.respone = None

	# main loop
	def create_lobby(self, player_count): # Find a way to ensure that only the player_count can join
		self.active = True

		try:
			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as e:
			print ("Socket creation failed: " + str(e))
			return
		try:
			server.bind((self.ip, self.port))
		except socket.error as e:
			print ("Failed to bind socket: " + str(e))
			return

		server.settimeout(self.timeout)
		server.listen()

		while self.active:
			conn, addr = server.accept() # loop stalls on this until new connection
			self.connections.append(conn)
			client_thread = threading.Thread(self.handle_client, args=(conn, addr,))
			client_thread.start()

		server.close()

	def receive_action(self, conn):
		json = None
		json = conn.recv(4096) # do time out
		if (json != None):
			for rule in self.rules:
				if (self.verify_action(rule, json) == False):
					return False
			return True
		return False

	# Rule will be a function that the json will be fed into
	def verify_action(self, rule, json):
		pass

	def relay_action(self):
		for conn in self.connections:
			conn.send(self.response)

	# Rule is a function that somehow determines the next players turn
	def send_turn_permission(self, rule):
		pass

	# CORE FUNCTIONALITY ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	# Allow server shutdown
	def set_server_activity(switch):
		self.active = switch

	# Customize timeout
	def set_receive_timout(self, timeout):
		self.timeout = timeout

	# handle receive and relay of messages
	def handle_client(self, ip, conn):
		while self.active:
			if (self.receive_action(conn) and self.response != None): # returns false if not recieved or invalid response
				self.relay_action() # tell all connections the move
				self.reponse = None

		self.connections.remove(conn)
		conn.close()

	# allow for custom rules to be added for verify_action()
	def add_rule(self, func):
		self.rules.append(func)


if __name__ == "__main__":
	server = Server(timeout=1)
	server.create_lobby(4)
