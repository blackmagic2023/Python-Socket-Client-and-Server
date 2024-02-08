import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to listen on
host = "127.0.0.1"
port = 12345

try:
    # Bind the socket to the address
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print(f"Server is listening on {host}:{port}")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()

    print(f"Connection from {client_address}")

    # Send a message to the client
    client_socket.send(b"Hello, client!")

    # Receive data from the client
    data = client_socket.recv(1024)

    if data:
        print(f"Received from client: {data.decode('utf-8')}")
    else:
        print("Client disconnected.")

except socket.error as e:
    print(f"Error: {e}")

finally:
    # Close the sockets
    client_socket.close()
    server_socket.close()
