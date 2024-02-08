import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
server_host = "127.0.0.1"
server_port = 12345

try:
    # Connect to the server
    client_socket.connect((server_host, server_port))

    # Receive data from the server
    data = client_socket.recv(1024)

    if data:
        print(f"Received from server: {data.decode('utf-8')}")
    else:
        print("Server disconnected.")

    # Send a message to the server
    client_socket.send(b"Hello, server!")

except socket.error as e:
    print(f"Error: {e}")

finally:
    # Close the socket
    client_socket.close()
