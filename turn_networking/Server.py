"""
Features:
Lobby Creation
Receive Action
Verify Action
Relay Action
Send Turn Permission
"""

class Server:
	def __init__(self, ip="127.0.0.1", port=53849, timeout=0.1):
		self.ip = ip
		self.port = port

		self.connections = []

		self.timeout = timeout

	# This is the main loop?
	def create_lobby(self):
		pass

	def receive_action(self):
		pass

	# Rule will be a function that the json will be fed into
	def verify_action(self, rule):
		pass

	def relay_action(self):
		pass

	# Rule is a function that somehow determines the next players turn
	def send_turn_permission(self, rule):
		pass

	# CORE FUNCTIONALITY ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	def set_receive_timout(self, timeout):
		self.timeout = timeout

if __name__ == "__main__":
	server = Server(timeout=1)
	server.create_lobby()
