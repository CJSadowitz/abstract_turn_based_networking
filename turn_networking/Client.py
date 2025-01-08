"""
Features:
Send Action
Receive Turn Permission
Receive Other Client Actions
Join Lobby
Discover Lobbies
"""

class Client:
	def __init__(self, timeout=0.1):
		self.timeout = timeout

	# Main loop
	def join_lobby(self, ip, port):
		pass

	# returns all discovered ip's broadcasting information
	def discover_lobbies(self):
		pass

	# send json to the server for processing
	def send_action(self, json):
		pass

	# receive game state from server
	def receive_action(self):
		pass

	def set_timeout(self, timeout):
		self.timeout = timeout

if __name__ == "__main__":
	pass
