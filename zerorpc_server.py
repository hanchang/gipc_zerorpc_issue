import os

import zerorpc

class ZerorpcServer:
    def getpid(self):
        return os.getpid()

if __name__ == "__main__":
    try:
        print("Starting zerorpc_server...")
        zerorpc_server = ZerorpcServer()
        server = zerorpc.Server(zerorpc_server)
        server.bind("ipc:///tmp/test_zerorpc_server.sock")
        server.bind("tcp://127.0.0.1:8888")
        server.run()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)

