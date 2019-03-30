import select,socket,sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('0.0.0.0',9006))
s.send('CONNECT')

rlist = (sys.stdin,s)

while True:
        read,write,fail = select.select(rlist,(),())
        for sock in read:
            if sock==s:
                data = s.recv(4096)
                print(data.decode('utf-8'))
            else:
                msg = sock.readline().encode('utf-8')
                s.send(msg)
