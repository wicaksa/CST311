**PROGRAMMING ASSIGNMENT 3 MULTITHREADING SERVER**

**PURPOSE**: The purpose of this assignment is to satisfy one of the stated outcomes in the syllabus:
You will write the program in Python where the interface to the TCP/IP application programming
interface is similar to other C-family programming languages.**

**Client code**
There are two clients, X and Y that will communicate with a server. 
Clients X and Y will each open a TCP socket to your server and wait until the server establishes a 
connection with both the clients. In the next step, one of the clients sends a message to your server 
followed by the other client. The message contains the name of the client followed by a name 
(e.g., “Client X: Alice”, “Client Y: Bob”). Later clients receive a message back from the server, 
indicating which message arrived at the Server first and which arrived second. The clients should print 
the message that they sent to the server, followed by the reply received from the server. The following 
figures explain the problem.

**Server code**
The server will accept connections from both clients and after it has received messages from both X and Y, 
the server will print their messages and then send an acknowledgment back to your clients. The acknowledgment 
from the server should contain the sequence in which the client messages were received (“X: Alice received
before Y: Bob”, or “Y: Bob received before X: Alice”). After the server sends out this message it should output 
a message saying - “Sent acknowledgment to both X and Y”. Your server can then terminate.
The server sits in an infinite loop listening for incoming TCP packets. When a packet comes, the server simply 
sends it back to the client. You can use the TCP server/client programs from the previous programming assignment 
as templates to start and then modify it to build your
programming assignment.

**SCREENSHOTS**
<img width="1407" alt="1  Start Server" src="https://user-images.githubusercontent.com/50036161/136609884-6d9382cb-737e-4a06-958c-8c1ad9fde75b.png">
<img width="1404" alt="2  Connect First Client" src="https://user-images.githubusercontent.com/50036161/136609912-f55562a0-17c6-4a41-b2b7-2db7010368e0.png">
<img width="1397" alt="3  Connect Second Client" src="https://user-images.githubusercontent.com/50036161/136609914-43ac2fa9-819f-4438-a024-949c9d39842c.png">
<img width="1407" alt="4  First Message Client X" src="https://user-images.githubusercontent.com/50036161/136609915-f09ba4e3-3d25-4af5-a6c2-fa4cdea44b84.png">
<img width="1402" alt="5 Second Message From Client Y" src="https://user-images.githubusercontent.com/50036161/136609919-1ec882aa-e8c4-4bc3-abf7-66b9e50a37f0.png">
<img width="1422" alt="6  FIRST MESSAGE CLIENT Y" src="https://user-images.githubusercontent.com/50036161/136609921-7f0f8435-bee2-45c1-8805-5a7c87ef92dc.png">
<img width="1404" alt="7  SECOND MESSAGE CLIENT X" src="https://user-images.githubusercontent.com/50036161/136609923-7e2819fc-b995-4d36-8052-fafdb786b4ff.png">

**MEMBERS**
Wicaksa Munajat : Team Lead, Programmer
Cheuk On-Yim : Programmer
Matt Stoney : Programmer
Paola Torres : Programmer
