from web3 import Web3
import requests
import json
import rlp



class Server():
    def __init__(self):
        self.w3 = Web3()
        pass
    def __send_post(self,url, data):
        header = {'Content-Type':'application/json'}
        res = requests.post(url=url, data=data, headers= header)
        return res.json()
    def getTransaction(self,from_addr, to, data , value, gas, gasPrice, nonce = 0, chainId = 1):
        d = dict()
        d['chainId']= chainId
        d['nonce'] = nonce
        d['from'] = from_addr
        d['to'] = to
        d['gas'] = gas
        d['value'] = value
        d['data'] = data
        d['gasPrice'] = gasPrice
        return d

    def singTransaction(self, tx, key):
        sign = self.w3.eth.account.signTransaction(tx, key)
        return self.w3.toHex(sign["rawTransaction"])

    def __send_transaction(self, url, method, params):
        data = {"jsonrpc":"2.0","method":"","params":[],"id":1}
        data["method"] = method
        data["params"] = params
        re = self.__send_post(url, json.dumps(data))
        return re
    def getNonce(self,url, address):
        re = self.__send_transaction(url,"eth_getTransactionCount",[address,'latest'])
        if 'error' in re:
            return 0
        return re['result']
    def send_rawtransaction(self, url, data):
        return self.__send_transaction(url, "eth_sendRawTransaction", [data])

    def get_transactionByHash(self,url, hash):
        return self.__send_transaction(url, "eth_getTransactionByHash",[hash])

class Author():
    def __init__(self, addr ='', key = '', node_url =''):
        self.key = key
        if self.key !='':
            self.addr = Web3().eth.account.privateKeyToAccount(self.key).address
        else:
            self.addr = addr
        self.url = node_url
        self.server = Server()
    def getNonce(self):
        if self.url =='':
            raise Exception("error url")
        return self.server.getNonce(self.url, self.addr)
    def createTransaction(self,from_addr = '', to_addr='', value =0 , data ='', gas= 21000, gasPrice= 6, nonece_auto = True, nonce =0, chainId = 1):
        if nonece_auto:
            nonce = self.getNonce()
        return self.server.getTransaction(from_addr,to_addr, data, value, gas, gasPrice, nonce, chainId = chainId)

    def sendTransaction(self, tx):
        ditraw = Web3().eth.account.signTransaction(tx, self.key)
        raw = Web3().toHex(ditraw['rawTransaction'])
        print(raw)
        return self.server.send_rawtransaction(self.url, raw)


if __name__ == '__main__':
    url = 'http://127.0.0.1:8801'
    chainID =600
    acc = Author(key='0x991de187e4bebc7467e4ce2c1365be6cd74199634e356eea45018458113e4c2d', node_url=url)
    t = acc.createTransaction(from_addr='0x8Db0d0Dd0E1571c0d22F821fde96c7AF910A0b45',gas="0xfffff",gasPrice=100, to_addr="0x3789Ba57b337AA50F219DFDfbE62525f8CFA3b0c", chainId = chainID)
    print(t)
    re = acc.sendTransaction(t)
    print(re)

    #print(Server().get_transactionByHash(url, '0xfa1b1e3820f1a37755e8989b812259a535d7f009f5856bce5b3faeebae7d400b'))

