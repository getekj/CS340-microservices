import json
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 54290 # The port used by the server

client_info = {"action": "save", "path": "path.txt", "info": "You are millionare yay"}
client_info_json = json.dumps(client_info)

#creates the socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connects to the server at the host/port
    s.sendall(bytes(client_info_json, encoding="utf-8")) #sends the msg to the server, use send all to ensure entire msg sent
    data = s.recv(1024) #recieves msg from server, 1024 is the max amount of bytes that can be recieved at once
    # when bytes arrive, need to save them in a buffer because calling .recv() again reads the next stream of bytes

print(f"Received {data}")