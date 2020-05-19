import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(('127.0.0.1',5090))
    print('[+] Trying to connect with 127.0.0.1:5090')
    
    while True:
        data = input('Enter data to send: ')
        client_socket.send(data.encode())

        server_data = client_socket.recv(1024)
        if(server_data.decode()==''):
            print('[+] Server is disconnected...')
            break

        print('[+] Server sent: {}'.format(server_data.decode()))

except (ConnectionRefusedError):
    print('connection refused')

finally:
    client_socket.close()
