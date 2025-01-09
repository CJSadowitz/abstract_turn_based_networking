# Abstracted Networking Module
## Goal
Create a python module that can easily create an authoritative server and clients </br>
Intended for use in turn based games </br>
## Installation
Python Module: `pip install xxx` </br>
## Documentation
### Server
Functions:
- Receive action
- Verify action
- Relay action
- Send turn permission
- Lobby creation
### Client
Functions:
- Send action
- Receive other client(s) action
- Receive turn permission
- Join lobby
### Setup
Import Modules: `from Server import Server` and `from Client import Client` </br>
### Server
**Reorder the functions for user called functions and server called functions** </br>
Server is a class that you create an object of to run: </br>
Constructor: `s = Server(ip, port, timeout)` </br>
Functions:
- `s.add_rule(function)` </br>
Each function will be added to a list that is ran through verify_action function </br>
The rule function *must* return a bool true or false </br>
- `s.verify_action(rule, json)` </br>
A function that is automatically called by the server to check the validity of the json WRT the rule function </br>
- `s.set_receive_timeout` </br>
Allow customization of timeout after instantiation </br>
- `s.shutdown()` </br>
Closes all connections and turns off server </br>
- `s.relay_action()` *maybe change this to include the message?* </br>
Automatically called by server to send a message to each connected client </br>
- `s.receive_action(connection)` </br>
Returns a boolean; if there was valid received data, returns true; calls `verify_action(rule, json)` </br>
- `s.convert_game_state_function(function)` *maybe rename this* </br>
Pass in the function that will convert the received game state into the desired message to send to clients </br>
- `s.make_game_state(json)` </br>
Returns the converted message from the function provided in `s.conver_game_state_function(function)` </br>
- `s.create_lobby(player_count)` **THE function to call** </br>
Establishes a socket for clients to connect to: </br>
Throws: *something to be added* </br>
Handles client connection and thread creation for each client </br>
- `s.handle_client(ip, connection)` </br>
Server Handles receiving information and relaying valid information to other clients </br>
### Client
**Reoder for order of user called functions** </br>
Constructor: `c = Client(timeout)` </br>
Functions:
- `c.discover_lobbies()` **Still need to make this function** </br>
Returns list of ip and port numbers </br>
- `c.join_lobby(ip, port)` </br>
Main loop of client thread: </br>
Throws: *something to be added* </br>
Handles sending messages and Receiving messages </br>
- `c.set_message(json)` </br>
Allows the user to send a message to the server </br>
- `c.receive_action(connection)` </br>
Attempts to receive information from server </br>
Throws: *something to be added* </br>
- `c.set_timeout(timeout)` </br>
Allows for user customization of when the client will move on from waiting on a response from the server </br>
- `c.get_game_state()` </br>
Returns game_state received from server specified by user provided function for server code </br>
- `c.shutdown()` </br>
Closes client connection to the server </br>
