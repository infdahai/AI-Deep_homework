
from twisted.internet import protocol, reactor,endpoints

transports = set()
"""
class Chat(protocol.Protocol):
    def dataReceived(self, data):
        transports.add(self.transport)
        
        if ':' not in data:
            return
        user, msg = data.split(':', 1)
        
        for t in transports:
            if t is not self.transport:
                t.write('{0} says: {1}'.format(user, msg))

class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat()

#reactor.listenTCP(9096, ChatFactory())
endpoints.serverFromString(reactor,"tcp:9005").listen(ChatFactory)
reactor.run()

"""

from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:9006").listen(EchoFactory())
reactor.run()

