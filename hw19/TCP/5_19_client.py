import socket
while 1:
    try:
        sock = socket.socket()
        sock.connect(('localhost', 1337))
        sock.send(input("Insert domain name to resolve it into IP:\nOR\nInsert command 'hostadd %hostname%:x.x.x.x' where x represent ipv4 format:\n").encode())

        data = sock.recv(158)


        print(data.decode())
    except KeyboardInterrupt:
        sock.close()
        exit()