
from twisted.internet import protocol, reactor,endpoints

transports = set()

def esc_markup(msg):
    return (msg.replace('&', '&amp;')
            .replace('[', '&bl;')
            .replace(']', '&br;'))


from twisted.internet import protocol, reactor, endpoints
from api_use import Chat_API
import itertools

class Echo(protocol.Protocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._use_api = Chat_API()


    def dataReceived(self, data):
        #self.transport.write(data)
        # send data from turing api in utf-8 coding
        self.transport.write(str(self._use_api.run(data),"utf-8"))

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

# listen the 9006 port in tcp connection
endpoints.serverFromString(reactor, "tcp:9006").listen(EchoFactory())
reactor.run()

