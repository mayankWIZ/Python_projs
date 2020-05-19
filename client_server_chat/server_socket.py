import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',5090))
server_socket.listen()
print('[+] Listening on 127.0.0.1:5090')

def serve_client(con,addr):
    print('[+] Got connection from {}'.format(addr))
    try:
        while True:
            data = con.recv(1024)
            rdata = data.decode()
            if('tata' in rdata.split(' ')):
                con.send(b'')
                break
            print('[+] Client sent: {}'.format(rdata))

            server_data = input('Enter data to sent: ')
            con.send(server_data.encode())
        con.close()
        
    except (ConnectionRefusedError):
        print('Connection is aborted')

    except (ConnectionRefusedError):
        print('Connection Refused')

    finally:
        print('[+] Client {} disconnected...'.format(addr))

while True:

    con,addr = server_socket.accept()
    serve_client(con,addr)
