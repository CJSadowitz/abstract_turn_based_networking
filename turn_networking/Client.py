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

	def join_lobby(self, ip, port):
		pass

	def discover_lobbies(self):
		pass

	def send_action(self, json):
		pass

	def receive_action(self):
		pass

	# CORE FUNCTIONALITY ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	def set_timeout(self, timeout):
		self.timeout = timeout

if __name__ == "__main__":
	pass
