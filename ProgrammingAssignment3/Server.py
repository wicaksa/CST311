# Server.py

'''
# Group: Cheuk On-Yim, Matthew Stoney, Paola Torres, Wicaksa Munajat
# Date: 10/07/2021
# Title: Server.py
# Programming Assignment 3 
# CST311 CSUMB CS ONLINE FALL 2021

# Description: This TCP Server program that will connect to two different clients at the same time. 
# The server will wait until both connections are established. Then it will receive a message 
# fom each client, display the message sent by each client, and return messages back to both clients
# as to the order of the messages sent and who sent each message. 

Answer to question 11: Explain why you need multithreading to solve this problem. 

This program needs to be able to handle concurrent execution so that it can share data between threads. 
What multithreading does is that it allows the processor to "multitask" and allows for both clients 
that are connected to communicate with the server at the same time. If we didn't create a new thread
each time a connection is made in our server while condition, the server will not be able to take in 
more connections and therefore blocking other clients from trying to connect until that client is done. 
But because we created a new thread for each client that is connected, each client can run on their own 
and doesn't have to wait until the current client is finished with the connection.

'''

from socket import *
import threading

global clientName, receivedMessages, threads, clientDict
clientDict = {}
clientName = {}
receivedMessages = []
threads = []
threadCount = 0

def listenToClientMessages(clientSocket,addr):
    # If thread number is 1, call it client X
    serverMessage = ""
    clientLetter = ""

    # Differentiate which client has connected (X or Y)
    if threadCount == 1:
        serverMessage = 'From Server: Client X Connected'
        clientLetter = "X"
        print('Accepted first connection, calling it client ' + clientLetter)
    # If thread number is 2, call it client Y
    if threadCount == 2: 
        serverMessage = 'From Server: Client Y Connected'
        clientLetter = "Y"
        print('Accepted second connection, calling it client ' + clientLetter)

    # Tell the client that it connected to the server by sending it back a message.
    clientSocket.send(serverMessage.encode())
   
    # Save clientLetter and the socket 
    clientName[clientLetter] = clientSocket

    # Receive message from client
    clientMessage = clientSocket.recv(1024)
    
    # Add the message to the list
    receivedMessages.append(clientMessage.decode())

    # Add Letter and message to client Dict
    clientDict[clientLetter] = clientMessage.decode()

    # Print message on server side
    # if len of receivedMessages is 1, then the first client just sent a message
    if len(receivedMessages) == 1:
        print('Client ' + clientLetter + ' sent message 1: ' + receivedMessages[0])

    if len(receivedMessages) == 2:
       print('Client ' + clientLetter + ' sent message 2: ' + receivedMessages[1])

# check if both clients have sent messages, if so return back result to clients
    if(len(receivedMessages)==2):
        sendToAllClients()

# Send message to both clients 
def sendToAllClients():
    for (clientLetter,clientSocket) in clientName.items():
        for key in clientName:
            if clientDict.get(key) == receivedMessages[0]:
                clientLetter1 = key
            if clientDict.get(key) == receivedMessages[1]:
                clientLetter2 = key
        message = 'From Server: ' + clientLetter1 + ' : ' + receivedMessages[0] + ' received before ' + clientLetter2 +  ' : ' + receivedMessages[1]
        clientSocket.send(message.encode())
        clientSocket.close()

# This function returns the serverSocket.
def getServerSocket():
    # Get Server Name and Port
    serverName = gethostbyname(gethostname())
    serverPort = 12000

    # Bind server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))

    # Waiting for client to connect
    print('The server is waiting to receive 2 connections..', "\n")
    serverSocket.listen(1)

    return serverSocket

# This function starts up the server and listens for connections from clients. 
def listenToNewConnections(serverSocket):
    global threadCount
    threadCount = 0

    while threadCount!=2:
        clientSocket,addr = serverSocket.accept()

        # Increment Thread Count
        threadCount+=1

        # Create a new thread when you connect with a client so other client can connect
        t = threading.Thread(target=listenToClientMessages, args=[clientSocket, addr])

        threads.append(t)

        # start the thread
        t.start()

# This is the main function.
def main():
    global clientName,receivedMessages
    
    # Initialize server socket to listen to connections
    serverSocket = getServerSocket()

    # start listening to new connections
    listenToNewConnections(serverSocket)
    
    # Once both clients have connected, wait until both have sent a message.
    print("\n")
    print("Waiting to receive messages from client X and Client Y", "\n")

    # Join threads
    for t in threads:
        t.join()

    print("\n")
    print("Waiting a bit for clients to close their connections.")
    print("Done.", "\n")

    # Close server
    serverSocket.close()

if __name__ == "__main__":
    main()
    

