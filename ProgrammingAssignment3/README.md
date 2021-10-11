# PROGRAMMING ASSIGNMENT 3 MULTITHREADED SERVER

# PURPOSE 
The purpose of this assignment is to write the program in Python where the interface to the TCP/IP application programming
interface is similar to other C-family programming languages.

# Client Code
There are two clients, X and Y that will communicate with a server. 
Clients X and Y will each open a TCP socket to the server and wait until the server establishes a 
connection with both the clients. In the next step, one of the clients sends a message to your server 
followed by the other client. The message contains the name of the client followed by a name. 
Later clients receive a message back from the server, indicating which message arrived at the Server first 
and which arrived second. The clients should print the message that they sent to the server, followed by the 
reply received from the server.

# Server Code
The server will accept connections from both clients. After it has received messages from both X and Y, 
the server will print their messages and then send an acknowledgment back to the clients. The acknowledgment 
from the server should contain the sequence in which the client messages were received (“X: Alice received
before Y: Bob”, or “Y: Bob received before X: Alice”). After the server sends out this message it should output 
a termination message before the server can then terminate.

# Screenshots
<img width="1115" alt="1  Server Started" src="https://user-images.githubusercontent.com/50036161/136730107-cee187f9-1ab5-4177-a5ed-359e2150cb48.png">
<img width="1117" alt="2  First Client Connected" src="https://user-images.githubusercontent.com/50036161/136730109-b3456e84-1401-4c99-b744-ae70e5a792f7.png">
<img width="1113" alt="3  Second Client Connected" src="https://user-images.githubusercontent.com/50036161/136730110-0d6c8745-0314-4732-9871-efb3131a757e.png">
<img width="1112" alt="4  X Sends Message 1" src="https://user-images.githubusercontent.com/50036161/136730111-c83fa261-b340-4607-8019-18defc0a8ac6.png">
<img width="1154" alt="5  Y Sends Message 2" src="https://user-images.githubusercontent.com/50036161/136730114-358b51c4-87e7-46b6-960d-62184e6901dc.png">
<img width="1157" alt="6  Y Sends Message 1" src="https://user-images.githubusercontent.com/50036161/136730115-630bd897-5102-4c5c-9068-383573e6900f.png">
<img width="1153" alt="7  X Sends Message 2" src="https://user-images.githubusercontent.com/50036161/136730117-c70edea5-7a0d-44f5-9592-05da80a23fb0.png">

# Team Members
Wicaksa Munajat : Team Lead, Programmer\
Cheuk On-Yim : Programmer\
Matt Stoney : Programmer\
Paola Torres : Programmer
