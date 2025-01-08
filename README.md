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
</br>
### Client
Functions:
- Send action
- Receive other client(s) action
- Receive turn permission
- Join lobby
</br>
### Setup
Import Modules: `from Server import Server` and `from Client import Client`
### Functions
Server is a class that you create an object of to run:
Constructor: `server = Server()`

