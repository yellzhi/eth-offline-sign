import json

import requests
headers = {'content-type': 'application/json'}
def post(url, method, params, timeout = 2):
    payload ={
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 1,
    }
    try :
        response = requests.post(url, data=json.dumps(payload), headers=headers, timeout= timeout).json()
    except Exception as e:
        print("server timeout connect field")
        return None
    return response

class Client():
    def __init__(self, nodeUrl):
        self.nodeUrl = nodeUrl
        self.use = False
        if self.getBlockNum(timeout=5) is not None:
            self.use = True

    def getBlockNum(self, timeout =2):
        ret = post(self.nodeUrl, "eth_blockNumber", [], timeout =timeout)
        if ret is None or "result" not in ret:
            return None
        return ret["result"]
    def getNonce(self, address):
        ret = post(self.nodeUrl, "eth_getTransactionCount",[address,'latest'], timeout=2)
        if ret is None or "result" not in ret:
            return 0
        return ret["result"]
if __name__ == '__main__':
    c = Client("http://127.0.0.1:8801")
    c.getBlockNum()




