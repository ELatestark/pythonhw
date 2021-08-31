import socket
import validators
import dns.resolver


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

while 1:

    sock = socket.socket()
    sock.bind(('', 1337))
    sock.listen(1)
    conn, addr = sock.accept()

    try:
        data = conn.recv(158).decode()
        if data.startswith("hostadd "):
            out_file = open('hosts', 'a')
            if validate_ip(data.split(':')[1]):
                out_file.write(data.replace('hostadd ','') + '\n')
                conn.send('Host added.'.encode())
            else:
                conn.send('Incorrect IP'.encode())
        elif validators.url('http://'+data):
            resolve_ip = dns.resolver.resolve(data, 'A')
            for resolver_ip in resolve_ip:
                conn.send(str(resolver_ip).encode())
        else:
                out_file = open('hosts', 'r')
                hosts_lines = out_file.readlines()
                for line in hosts_lines:
                    if data == line.split(':')[0]:
                        conn.send(line.split(':')[1].encode())
                else:
                    conn.send('No such record or site unavailable.'.encode())
    except KeyboardInterrupt:
        out_file.close()
        conn.close()
        exit()
