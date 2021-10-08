# Client.py

# Group: Cheuk On-Yim, Matthew Stoney, Paola Torres, Wicaksa Munajat
# Date: 10/07/2021
# Title: Client.py
# Programming Assignment 3 
# CST311 CSUMB CS ONLINE FALL 2021

# Description: This is a TCP Client program that will connect to a client. 
# It will send a message inputted by the user to the client. 

from socket import *
import sys
import threading

global clientName, received

# connect with server at port
def getConnection(serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

# method to send message to server
def sendMessages(clientSocket):
    global clientMessage
    clientMessage = input('Enter Message to send to Server: ')
    clientSocket.send(clientMessage.encode())

# receive message from server
def receiveMessages(clientSocket):
    serverMessage = clientSocket.recv(1024)
    print(serverMessage.decode())


def main():
    # Get server name and server port
    serverName = gethostbyname(gethostname())
    serverPort = serverPort = 12000

    # Get Client Socket
    clientSocket = getConnection(serverName,serverPort)

    ## Start your thread
    ##t.start()

    # Receive message when you connect to server.
    receiveMessages(clientSocket)

    # Send message to server
    sendMessages(clientSocket)

    # Receive Message back from the server after both connections.
    receiveMessages(clientSocket)

    # Close socket
    # clientSocket.close()

if __name__ == "__main__":
    main()
    
