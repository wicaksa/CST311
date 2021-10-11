# Client.py

# Group: Cheuk On Yim, Matthew Stoney, Paola Torres, Wicaksa Munajat
# Date: 10/07/2021
# Title: Client.py
# Programming Assignment 3 
# CST311 CSUMB CS ONLINE FALL 2021

# Description: This is a TCP Client program that will connect to a server. 
# It will send a message inputted by the user to the server. 

from socket import *
import sys
import threading

# This function creates a clientSocket and returns it. 
# Input : serverName : String
#         serverPort : int
# Output: socket object 
def getConnection(serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

# This function sends message to connected server.
# Input : clientSocket : socket object
# Output: None
def sendMessages(clientSocket):
    global clientMessage
    clientMessage = input('Enter Message to send to Server: ')
    clientSocket.send(clientMessage.encode())

# This function receives messages from the server and prints it out. 
# Input : clientSocket : socket object
# Output: None
def receiveMessages(clientSocket):
    serverMessage = clientSocket.recv(1024)
    print(serverMessage.decode())

# This is the main function.
def main():
    # Get server name and server port.
    serverName = gethostbyname(gethostname())
    serverPort = serverPort = 12000

    # Get Client Socket.
    clientSocket = getConnection(serverName,serverPort)

    # Receive message when you connect to server.
    receiveMessages(clientSocket)

    # Send message to server inputted by the user.
    sendMessages(clientSocket)

    # Receive Message back from the server after both connections have been made.
    receiveMessages(clientSocket)

# Call to main
if __name__ == "__main__":
    main()
    
