from twisted.internet import reactor, ssl
from twisted.web import server
import traceback

from jsonrpc.server import ServerEvents, JSON_RPC
class ExampleServer(ServerEvents):
    # inherited hooks
    def log(self, responses, txrequest, error):
        print(txrequest.code, end=" ")
        if isinstance(responses, list):
            for response in responses:
                msg = self._get_msg(response)
                print(txrequest, msg)
        else:
            msg = self._get_msg(responses)
            print(txrequest, msg)

    def findmethod(self, method, args=None, kwargs=None):
        if method in self.methods:
            return getattr(self, method)
        else:
            return None

    # helper methods
    methods = set(["add", "subtract"])

    def _get_msg(self, response):
        #print("response", repr(response))
        return " ".join(
            str(x) for x in [response.id, response.result or response.error]
        )

    def subtract(self, a, b):
        return a - b

    def add(self, a, b):
        return a + b


root = JSON_RPC().customize(ExampleServer)
site = server.Site(root)

# if __name__ == '__main__':
#     # 8007 is the port you want to run under. Choose something >1024
#     PORT = 8007
#     print("Listening on port %d..." % PORT)
#     reactor.listenTCP(PORT, site)
#     reactor.run()
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher


@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('localhost', 4000, application)




