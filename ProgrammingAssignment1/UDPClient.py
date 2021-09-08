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

TEST CASES:
abcdef
abc123def
ABcdEF
AB12cdEF
Two Words HERE !!
'''

# Import socket module
from socket import *

# DNS automatic lookup of hostname to get IP address
SERVER_NAME = gethostbyname(gethostname())
# Set server port number to 12000
SERVER_PORT = 12000
ADDR = (SERVER_NAME, SERVER_PORT)

# Create a client socket
# family AF_INET = IPv4
# type SOCK_DGRAM = UDP Socket
clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

# Prompt user to input lowercase sentence and save it into a variable
message = input('Input lowercase sentence:')

# Send message through the socket to the destination host
# Encode message from string type to -> byte with encode()
clientSocket.sendto(message.encode(), ADDR)

# When packet arrives from the internet at the client's socket
# Packet data is put into modifiedMessage
# serverAddress contains (server's IP, Port number)
# Buffer size of 2048 works for most purposes
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Print the message received.
print(modifiedMessage.decode())

# Close the connection.
clientSocket.close()