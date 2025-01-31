"""
Features:
Send Action
Receive Turn Permission
Receive Other Client Actions
Join Lobby
Discover Lobbies
"""

import socket
import time

class Client:
	def __init__(self, timeout=1):
		self.timeout = timeout
		self.active = False
		self.message = None
		self.game_state = None
		self.discover_active = False

		self.lobbies = []

	# Main loop
	def join_lobby(self, ip="127.0.0.1", port=53849):
		try:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as e: # add a throw here too?
			print ("Failed to create socket: " + str(e))
		try:
			client.connect((ip, port))
		except Exception as e: # add a throw here too?
			print ("Failed to make connection with " + ip + " :" + str(e))

		self.active = True

		while self.active:
			if self.message != None:
				client.send(self.message.encode("utf-8"))
				self.message = None
			self.receive_action(client)

		client.close()

	# send json to the server for processing
	def set_message(self, json):
		self.message = json

	# receive game state from server
	def receive_action(self, client):
		client.settimeout(self.timeout) # Consider moving this for efficiency?
		try:
			self.game_state = client.recv(4096).decode("utf-8")
			print ("CLIENT: ", self.game_state)
		except socket.timeout:
			pass # Maybe change this to a throw such that the user can handle this?
		except KeyboardInterrupt:
			client.close()

	def set_timeout(self, timeout):
		self.timeout = timeout

	# returns game state for use outside of client code
	def get_game_state(self):
		return self.game_state

	def shutdown(self):
		self.active = False

	def shutdown_discover(self):
		self.discover_active = False

	# Port should be same but customizable
	def discover_lobbies(self):
		self.discover_active = True

		discover = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		discover.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		discover.bind(("", 5000))

		while self.discover_active:
			data, addr = discover.recvfrom(1024)
			lobby = data.decode("utf-8")
			if lobby in self.lobbies:
				continue
			else:
				self.lobbies.append(lobby)
			time.sleep(5)
