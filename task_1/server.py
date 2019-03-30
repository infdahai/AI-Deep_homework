
from twisted.internet import protocol, reactor,endpoints
colors = ['7f8c8d', 'c0392b', '2c3e50', '8e44ad', '27ae60']
transports = set()

def esc_markup(msg):
    return (msg.replace('&', '&amp;')
            .replace('[', '&bl;')
            .replace(']', '&br;'))
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
from api_use import Chat_API
import itertools

class Echo(protocol.Protocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._use_api = Chat_API()

    def connectionMade(self):
        self.color = next(colors)

    def dataReceived(self, data):
        self.transport.write(self._use_api.run(data).encode('utf-8'))

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:9006").listen(EchoFactory())
reactor.run()

