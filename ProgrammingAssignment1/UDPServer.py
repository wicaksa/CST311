# Name : Wicaksa Munajat
# Class: CST311 - Intro to Internet Networks CSUMB F'21
# Date : Wednesday September 8, 2021
# DUe  : Tuesday September 14 @ 11:59pm

'''
This assignment shows the basics of socket programming for UDP and TCP using Python.
This assignment shows how to send and receive datagram packets using UDP and TCP sockets.
This assignment familiarizes student with a Client-Server architecture.

1. The client reads a line of characters (data) from its keyboard and sends the data to the server.
2. The server receives the data and converts the characters to uppercase.
3. The server sends the modified data to the client.
4. The client receives the modified data and displays the line on its screen.


'''

from socket import *

SERVER_PORT = 12000
serverSocket = socket(family=AF_INET, type=SOCK_DGRAM)
ADDR = (gethostbyname(gethostname()), SERVER_PORT)
# Bind SERVER_PORT to the Socket
serverSocket.bind(('', SERVER_PORT))

print("[SERVER IS RUNNING]...")
# UDPServer then enters a while loop;
# The while loop will allow UDPServer to receive and process packets from clients indefinitely.
# In the while loop, UDPServer waits for a packet to arrive
while True:
    BUFF_SIZE = 2048
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # Convert message to uppercase
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
