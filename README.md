# ReverseSSH

Following a Python networking tutorial found here: [YouTube Playlist](https://www.youtube.com/playlist?list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF).

Reverse SSH allows one computer to establish a connection onto another computer, and gain control without necessarily having been given permission.

The `server.py` file runs first, listening for any connections. This server script is running on the host.
When `client.py` runs (containing the ip address of the host), a connection is established. This connection is from the client to the host (Client -> Host).
Using this connection in the other direction (Client <- Host) is why it's called Reverse SSH - we're reversing the initial SSH connection direction.

In our code, the `server.py` file contains `s.accept()` to accept new connections. This method returns a new `Socket` object [[1]](https://docs.python.org/2/library/socket.html#socket-objects), which contains a connection which the server can use to send data back to the client.

To summorise: a client connects to the server, the server uses this connection to send data back over that connection.

