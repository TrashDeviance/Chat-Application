# Hunter Jackson and Matthew Hosier
# In order to use the colorama library you need to run this command>>> pip install colorama

import socket
from _thread import *
from _thread import *
import threading

# import colorama
# from colorama import Fore

serverHost = '127.0.0.1'  # local host address
serverPort = 12000  # port that will be listened on. Number from 1 - 65535 TCP port numbers
threadCount = 0

clients = []
userName = []

# Socket object for the server
server_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Broadcast a message from the server to all of the clients
def server_to_client(communicate):
    x = clients
    for x in clients:
        if x.send(communicate):
            return True
        else:
            return False


try:
    server_object.bind((serverHost, serverPort))  # Associates a local address with a socket
    server_object.listen()  # Listen for incoming connections from the client or clients
except socket.error as error:
    print(range(len(error)))


# Handle function for the clients
def handle_clients(handle_client):
    while True:
        try:
            # communicate = handle
            # handle.send(str.encode('Successful'))
            communicate = handle_client.recv(1024)
            server_to_client(communicate)
            # response = 'Message from server' + data.decode('utf-8')
        except:
            position = clients.index(handle_client)
            clients.remove(handle_client)
            handle_client.close()
            username = userName[position]
            server_to_client(f'{username} left the chat!'.encode('utf-8'))
            userName.remove(username)
            # handle.sendall(str.encode(response))
            # connection.close()
            break


# Receive function for the server. Will allow clients to join the chatroom
def receive():
    while True:
        print('The server is running now!')
        conn, address = server_object.accept()
        print(f"connected {str(address)}")

        # Will append the clients and their usernames
        conn.send('Press any key to continue'.encode('utf-8'))
        username = conn.recv(1024).decode('utf-8')
        userName.append(conn)
        clients.append(conn)

        server_to_client(f'{username}' 'has joined!'.encode('utf-8'))
        print(f'{username}' 'is connected to the server!')
        # server_to_client(f'{username}' ' has joined!'.encode('utf-8'))
        conn.send('Success!'.encode('utf-8'))

        # print(f'{username}' 'has disconnected from the server!')

        # Threading is used to run multiple tasks
        thread = threading.Thread(target=handle_clients, args=(conn,))
        thread.start()


receive()


# helpful sources
# https://dev.to/zeyu2001/build-a-chatroom-app-with-python-44fa
# https://realpython.com/python-sockets/
