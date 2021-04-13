from web3 import Web3
import base58


def getAccount(num):
    arr = []
    for _ in range(0, num):
        p = Web3().eth.account.create()
        d =dict()
        d["address"] = p.address
        d["privateKey"] = Web3.toHex(p.privateKey)
        d["bas58Key"] = Web3.toText(base58.b58encode(p.privateKey))

        arr.append(d)
    return arr


def sinTransactionWithNonce():
    pass


def singTransaction():

    pass

def sinTransactionAndSend():
    pass
