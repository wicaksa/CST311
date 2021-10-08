# Programming Assignment 2: UDP Pinger

# Program
In this assignment, you will learn the basics of socket programming for UDP in Python. 
You will learn how to send and receive datagram packets using UDP sockets and also, how to set 
a proper socket timeout. Throughout the assignment, you will gain familiarity with a Ping application 
and its usefulness in computing statistics such as packet loss rate.

# Client Code
The client should send 10 pings to the server. Since this is transmitted using UDP, packets might be lost
in the network so the client should only wait up to 1 sec for a reply before determining that the packet is lost.
The client also needs to calculate round-trip time, minimum, maximum, average RTTs, along with packet lost, and
packet loss rate. Also, it will print estimatedRTT, DevRTT, and timeout interval. 
