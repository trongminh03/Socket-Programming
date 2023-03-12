import socket

# Define the IP address and port for the server
ip_address = '127.0.0.1'
port = 5000

# Create a UDP socket object
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
udp_socket.bind((ip_address, port))

print('UDP server is listening on {}:{}'.format(ip_address, port))

while True:
    # Receive data from the client
    data, client_address = udp_socket.recvfrom(1024)

    # Print the received data and client address
    print('Received data: {}'.format(data.decode()))
    print('Client address: {}:{}'.format(client_address[0], client_address[1]))

    # Send a response to the client
    # response = 'Hello, client!'
    response = data.decode().upper()
    udp_socket.sendto(response.encode(), client_address)