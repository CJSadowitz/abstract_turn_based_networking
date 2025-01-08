"""
Features:
Send Action
Receive Turn Permission
Receive Other Client Actions
Join Lobby
Discover Lobbies
"""

import socket

class Client:
	def __init__(self, timeout=1):
		self.timeout = timeout
		self.active = False

		self.message = None
		self.game_state = None

	# Main loop
	def join_lobby(self, ip="127.0.0.1", port=53850):
		try:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as e:
			print ("Failed to create socket: " + str(e))
		try:
			client.connect((ip, port))
		except Exception as e:
			print ("Failed to make connection with " + ip + " :" + str(e))

		self.active = True

		while self.active:
			if self.message != None:
				client.send(self.message.encode())
				self.message = None
			self.receive_action(client)
			print ("Is Active")

		client.close()
		print ("Client Closed")

	# returns all discovered ip's broadcasting information
	def discover_lobbies(self):
		pass

	# send json to the server for processing
	def set_message(self, json):
		self.message = json

	# receive game state from server
	def receive_action(self, client):
		client.settimeout(self.timeout)
		try:
			client.recv(4096)
		except socket.timeout:
			print ("Client Timed out")
		except KeyboardInterrupt:
			client.close()

	def set_timeout(self, timeout):
		self.timeout = timeout

	# returns game state for use outside of client code
	def get_game_state(self):
		return self.game_state

	def shutdown(self):
		self.active = False

if __name__ == "__main__":
	pass
