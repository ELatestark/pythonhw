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

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 1337))
    conn, addr = sock.recvfrom(158)

    try:
        data = conn.decode()
        if data.startswith("hostadd "):
            out_file = open('hosts', 'a')
            if validate_ip(data.split(':')[1]):
                out_file.write(data.replace('hostadd ', '') + '\n')
                sock.sendto('Host added.'.encode(), addr)
            else:
                sock.sendto('Incorrect IP'.encode(), addr)
        else:
            out_file = open('hosts', 'r')
            hosts_lines = out_file.readlines()
            for line in hosts_lines:
                if data == line.split(':')[0]:
                    sock.sendto(line.split(':')[1].encode(), addr)
                    break
            else:
                if validators.url('http://' + data):
                    resolve_ip = dns.resolver.resolve(data, 'A')
                    for resolver_ip in resolve_ip:
                        sock.sendto(str(resolver_ip).encode(), addr)
                else:
                    sock.sendto('No such record or site unavailable.'.encode(), addr)

    except KeyboardInterrupt:
        out_file.close()
        sock.close()
        exit()
