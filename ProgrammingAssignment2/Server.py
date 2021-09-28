# Team 2: Cheuk On Yim, Matt Stoney, Paola Torres, Wicaksa Munajat
# CST311 Intro to Computer Networks Fall 2021
# Team Programming Assignment 2 Client Code

# ------------ Program -------
# Import modules
from socket import *
import time

def printResult(minRTT, maxRTT, totalRTT, packetReceived, packetLoss, estimatedRTT, devRTT):
    # Prints the result of our data for the following:
    # Print Out Min RTT, Max RTT, Avg RTT, Packet Loss %, Estimated RTT, Dev RTT, Timeout Interval

    # 1). Min RTT
    print(f'Min RTT:          {minRTT * 1000} ms')

    # 2). Max RTT
    print(f'Max RTT:          {maxRTT * 1000} ms')

    # 3). Avg RTT
    print(f'Avg RTT:          {(totalRTT / packetReceived) * 1000} ms')

    # 4). Packet Loss %
    print(f'Packet Loss:      {packetLoss * 10}%')

    # 5). Estimated RTT
    # estimatedRTT = (.875)*e(stimatedRTT) + .125(sampleRTT)
    print(f'EstimatedRTT:     {estimatedRTT * 1000}')

    # 6). Dev RTT
    # DevRTT = (1 - 0.25)*DevRTT + (0.25)*abs(SampleRTT - EstimatedRTT)
    print(f'DevRTT:           {devRTT * 1000}')

    # 7). Timeout Interval
    # timeOutInterval = EstimatedRTT + 4*DevRTT
    print(f'Timeout Interval: {(estimatedRTT + 4 * devRTT) * 1000}')

def printReceivedMessage(message, messageReceived, startTime, endTime, elapsedTime):
    # Prints the messages if received
    print(f'Mesg sent: {message}')
    print(f'Mesg rcvd: {messageReceived.decode()}')

    # Convert times to sci notation
    print('Start time: ' + "{:e}".format(startTime))
    print('Return time: ' + "{:e}".format(endTime))

    # Time in milliseconds so mult seconds by 1000
    print(f'{message} RTT: {elapsedTime * 1000} ms', "\n")

def printMessageLost(message, ping):
    # Prints message if packet is lost
    print(f'Mesg sent: {message}')
    print('No Mesg rcvd')
    print(f'PING {ping} Request Timed Out', "\n")

def main():
    # Get SERVER_NAME
    SERVER_NAME = gethostbyname(gethostname())

    # Set server port number to 12000
    SERVER_PORT = 12000

    # Keep track of minRTT, maxRTT, avgRTT, packetLoss, packetReceived
    minRTT = 1
    maxRTT = 0
    totalRTT = 0
    packetLoss = 0
    packetReceived = 0
    # In case packet 1 is lost
    # # you have to set the initial value when you do receive a packet back
    hasInitialValue = False

    # The client should send 10 pings to the server.
    for ping in range(1, 11, 1):

        # Create a client socket
        clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

        # Client waits up to one second for a reply;
        clientSocket.settimeout(1)

        # Also print the message that is sent to the server.
        message = 'Ping' + str(ping)

        # Set socket address which is a tuple (server name, port #)
        ADDRESS = (SERVER_NAME, SERVER_PORT)

        # Start the timer
        startTime = time.time()

        # Send ping message to server
        clientSocket.sendto(message.encode(), ADDRESS)

        try:
            # if no reply is received within one second, assume packet is lost
            messageReceived, server = clientSocket.recvfrom(1024)

            # Stop the timer
            endTime = time.time()

            # Calculate time elapsed between sent and received message
            elapsedTime = (endTime - startTime)

            # Keep track of minRTT, maxRTT, avgRTT, packetLoss
            if (elapsedTime < minRTT):
                minRTT = elapsedTime

            if (elapsedTime > maxRTT):
                maxRTT = elapsedTime

            # Leave out lost packets from avg calculation ie) if time is above 1 sec
            if (elapsedTime < 1):
                totalRTT += elapsedTime

            # Keep track of Estimated RTT and Dev RTT
            # If it's the first ping, set the initial value of the RTT

            if (ping == 1 or not hasInitialValue):
                estimatedRTT = elapsedTime
                devRTT = (estimatedRTT/2)
                hasInitialValue = True
            else:
                estimatedRTT = (.875*estimatedRTT) + (.125*elapsedTime)
                devRTT = (0.75 * devRTT) + (0.25 * abs(elapsedTime - estimatedRTT))

            # Keep track of the packets received
            packetReceived += 1

            # Print the messages if received
            printReceivedMessage(message, messageReceived, startTime, endTime, elapsedTime)

        # If time > 1s, message is lost
        except timeout:
            packetLoss += 1
            printMessageLost(message, ping)

    printResult(minRTT, maxRTT, totalRTT, packetReceived, packetLoss, estimatedRTT, devRTT)

# Call to main()
if __name__ == "__main__":
    main()
