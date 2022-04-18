# Hunter Jackson and Matthew Hosier
# In order to use the colorama library you need to run this command>>> pip install colorama
import sys
import socket
import threading

import colorama
from colorama import Fore, Back, Style
colorama.init()

# print(Fore.GREEN)

serverHost = '127.0.0.1'  # local host address
serverPort = 12000  # port that will be listened on. Number from 1 - 65535 TCP port numbers

userName = input(Fore.GREEN + "Choose a Name: " + Style.RESET_ALL)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(Fore.GREEN + "Connection established!" + Style.RESET_ALL)


try:
    client.connect(('127.0.0.1', 12000))  # Socket trying to connect to the local host and port
except socket.error as err:
    print(str(err))

# Receive function for the client to communicate
def receive():
    while True:
        try:
            communicate = client.recv(2048).decode('utf-8')
            if communicate == 'USERNAME':
                client.send(userName.encode('utf-8'))
            else:
                print(communicate)
        except:
            client.close()
            break


# The send function will handle the successful communication between the server and client
def send():
    while True:
        communicate = input()
        if communicate == 'Exit':  # If statement used for the client to type Exit to disconnect
            client.close()
            exit()
        else:
            print("Type 'Exit' to disconnect from the server!")
        communicate = f'{Fore.RED + userName + Style.RESET_ALL}: {communicate}'
        client.sendall(communicate.encode('utf-8'))


# print("Press any key to join the chat!")

# used to run the tasks for for the receive and send functions
thread_receive = threading.Thread(target=receive)
thread_receive.start()

thread_send = threading.Thread(target=send)
thread_send.start()



