from jsonrpc.jsonrpc2 import JSONRPC20Response
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

from server import account
from server import client
from server import transaction


class Server():
    def __init__(self, nodeUrl, listen, port):
        self.nodeUrl = nodeUrl
        self.listen = listen
        self.port = port
        self.dispatcher = dispatcher
        print("new a Server and try connect node:", nodeUrl)
        self.Node = client.Client(self.nodeUrl)
        if not self.__checkNode():
            print("node can not connect and only to sing ")
        else:
            print("node connect ok and can send transaction")
        self.tr = transaction.Server()
    def __checkNode(self):
        return self.Node.use
        pass

    def signTraction(self, data, key):
        if "gas" not in data:
            data["gas"] = 21000
        if "gasPrice" not in data:
            data["gasPrice"] = 6
        if self.__checkNode():
            data["nonce"] = self.Node.getNonce(data["from"])
        elif "nonce" not in data:
            data["nonce"] = 0
        d = dict()
        d["trasaction"] =data
        d["sign"]= self.tr.singTransaction(data, key)
        return d

    def singAndSend(self, data, key):
        sing = self.signTraction(data, key)
        ret = self.tr.send_rawtransaction(self.nodeUrl, sing['sign'])
        if "result" in ret:
            sing["txHash"] = ret["result"]
        else:
            sing["error"] = ret["error"]
        return sing

    def getAccount(self, num):
        print(self.nodeUrl)
        return account.getAccount(num)

    @Request.application
    def applicaction(self, request):
        self.dispatcher["getAccount"] = self.getAccount
        self.dispatcher["sign"] = self.signTraction
        self.dispatcher["signSend"] = self.singAndSend
        response = JSONRPCResponseManager.handle(
            request.get_data(cache=False, as_text=True), self.dispatcher)
        return Response(response.json, mimetype='application/json'
                    )
    def run(self):
        run_simple(self.listen, self.port, application=self.applicaction, threaded=True)

