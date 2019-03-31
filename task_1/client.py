import select,socket,sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('0.0.0.0',9006))
s.send('CONNECT')
# establish socket connect


rlist = (sys.stdin,s)

while True:
        # send and receive 
        read,write,fail = select.select(rlist,(),())
        for sock in read:
            if sock==s:
                data = s.recv(4096)

            else:
                msg = sock.readline()
                s.send(msg)
               # s.send(str(msg,'utf-8'))
