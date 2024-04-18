import socket
import time

# Set the proxy server address and port
PROXY_ADDR = '127.0.0.1'
PROXY_PORT = 8080

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the proxy server address and port
sock.bind((PROXY_ADDR, PROXY_PORT))

# Listen for incoming connections
sock.listen(5)

print(f'Proxy server listening on {PROXY_ADDR}:{PROXY_PORT}')

while True:
    # Accept a new connection
    client_sock, addr = sock.accept()

    # Log the client's IP address
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open('proxy_logs.txt', 'a') as f:
        f.write(f'{timestamp} - {addr[0]}\n')

    # Get the request from the client and decode it
    request = client_sock.recv(1024).decode('utf-8')

    # Check if the request is in the expected format
    if ':' not in request or '/' not in request:
        print(f'Invalid request format: {request}')
        continue

    # Parse the request to get the destination address and port
    parts = request.split(':')
    if len(parts) < 2:
        print(f'Invalid request format: {request}')
        continue

    destination_addr_port = parts[1].split('/')
    if len(destination_addr_port) < 2:
        print(f'Invalid request format: {request}')
        continue

    destination_addr = destination_addr_port[0]
    destination_port = int(destination_addr_port[1])

    # Create a new socket to connect to the destination server
    destination_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the destination server
    destination_sock.connect((destination_addr, destination_port))

    # Send the request to the destination server
    destination_sock.sendall(request.encode('utf-8'))

    # Receive the response from the destination server
    response = destination_sock.recv(1024)

    # Send the response back to the client
    client_sock.sendall(response)

    # Close the sockets
    client_sock.close()
    destination_sock.close()
