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
serverPort = 12000

# Creates a TCP socket.
serverSocket = socket(family=AF_INET, type=SOCK_STREAM)

# Associate the server port number, serverPort, with this socket:
serverSocket.bind(('', serverPort))

# Listen for TCP connection requests from the client.
# The parameter specifies the maximum number of queued connections (at least 1).
serverSocket.listen(1)

# Show that the server is running.
print('[SERVER IS RUNNING...]')

while True:
    # Invokes the accept() method for serverSocket.
    # This creates a new socket in the server, called connectionSocket.
    # The new socket is dedicated to this particular client.
    # Completes hand shake.
    connectionSocket, addr = serverSocket.accept()

    # Decode the message from Client.
    sentence = connectionSocket.recv(1024).decode()

    # Capitalize the sentence.
    capitalizedSentence = sentence.upper()

    # Send the new capitalizedSentence back to Client.
    connectionSocket.send(capitalizedSentence.encode())

    # Close the connection
    connectionSocket.close()


