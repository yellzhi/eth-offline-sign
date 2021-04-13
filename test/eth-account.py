from web3 import Web3
import base58
def test():
    p = Web3().eth.account.create()
    print(p.address)
    print(Web3.toHex(p.privateKey))
    bp = base58.b58encode(p.privateKey)
    print(bp)
    tbp = Web3.toText(bp)
    print(tbp)
    print((Web3.toHex(base58.b58decode(tbp))))

def getPeivateBybas58(b58s:[])->[]:
    p = []
    for b in b58s:
        pr = Web3.toHex(base58.b58decode(b))
        p.append(pr)
        print(Web3().eth.account.privateKeyToAccount(pr).address , pr)
        #print(Web3().eth.account.privateKeyToAccount(pr).address)
    #print(p)
    return p


def decodeConstract():
    inp = '0xe5ab4da20000000000000000000000006d989db3252bfe1e965779c22158624a4bd5ce650000000000000000000000000000000000000000000000000000000000001564'
    Web3().eth.defaultContractFactory.decode_function_input(inp)

if __name__ == "__main__":
    basePrivate =["5PBhnaYf4EiFPbymck48gz3JaSGo8jmn6bw2FF7Po69p",
                  "38edjFDWEiSHKwUsPgADYQVL2ucfTSCCNTWHgCVj2pzt",
                  "BJhofqPF8wvePrphMeYGk2jG9tDZPbuArZ6LDN8vx2Vi",
                  "3w6x9LhHpFaZ48bCTNZYZAyE5CNM8SmvnD4avJFy1T9C",
                  "6jMpVHXdwpM6sycVaQ9ZT5EoUUgmVLYzhqaxAe8ByKat",
                  "62Xg2zHhxnEgBc9MchZCn2ToVX1L4xtrRpgJ377ApnCz",
                  "7UznDSemWGLjMRGtByZs3RGkNg9gk3r9gR4HaFHTaU8n",
                  "AHnm88W7yQZhXpf15iWZcdaspQsoC7fFW2SkUjsXavrT",
                  ]
    getPeivateBybas58(basePrivate)

    print("test....")
    test()
