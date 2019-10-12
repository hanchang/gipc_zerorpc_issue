import os

import gipc
import zerorpc

class GipcZerorpcTest:
    def __init__(self):
        self._parent_state = 100
        # Uncommenting this line causes child subprocesses zerorpc_client to hang.
        # self.rpc_runner(0)
        self.subprocess_initializer()

    def subprocess_initializer(self):
        subprocesses = []
        for i in [1,2,3]: 
            print("Starting subprocess...")
            p = gipc.start_process(target=self.rpc_runner, args=(i,))
            subprocesses.append(p)
        for subprocess in subprocesses:
            subprocess.join()
        print("Finished!")

    def rpc_runner(self, input):
        print(f"Subprocess started with PID: {os.getpid()} and subprocess ID: {input} with parent state: {self._parent_state}")
        zerorpc_client = zerorpc.Client()
        zerorpc_client.connect("ipc:///tmp/test_zerorpc_server.sock")
        print(f"ZeroRPCServer PID: {zerorpc_client.getpid()}")

if __name__ == "__main__":
    try:
        print(f"Starting main process with PID: {os.getpid()}")
        gzt = GipcZerorpcTest()
        server = zerorpc.Server(gzt)
        server.bind("ipc:///tmp/gzt_server.sock")
        server.run()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)

