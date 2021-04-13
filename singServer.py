#! /usr/bin/env python
# coding = utf-8

import server.server as rpcServer
import argparse

def main(args):
    listen = "{0}".format(args.ip)
    port = int(args.port)
    node = "http://{0}".format(args.node)

    print("start server:\n",
          "listen:", listen, ":", port, "\n",
          "node:", node)

    se = rpcServer.Server(node, listen, port)
    se.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    parser.add_argument("-i","--ip", default="localhost", help="the server listen ip.", dest="ip")
    parser.add_argument("-p","--port", default=8089, help="the server listen port",  dest="port")
    parser.add_argument("-n","--node", default="localhost:8801", help="node address.",  dest="node")

    main(parser.parse_args())
    pass
