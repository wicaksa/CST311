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

from socket import *

serverName = gethostbyname(gethostname())
serverPort = 12000
ADDR = (serverName, serverPort)

# Create the client’s socket, called clientSocket.
# The first parameter again indicates that the underlying network is using IPv4
# The second parameter indicates that the socket is of type SOCK_STREAM, which is a TCP socket.
clientSocket = socket(family=AF_INET, type=SOCK_STREAM)

# Initiate the TCP connection between the client and server.
# Perform a 3-way-handshake and a TCP connection is established between the client and server.
clientSocket.connect(ADDR)

# Obtain a sentence from the user.
sentence = input('Input a lowercase sentence: ')

# Send the sentence through the client’s socket and into the TCP connection.
clientSocket.send(sentence.encode())

# When characters arrive from the server, they get placed into the string modifiedSentence.
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())

# Close the client’s socket.
clientSocket.close()