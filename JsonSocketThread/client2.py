# Python TCP Client A
import socket 
import sys
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940
#連續發訊息

class ConnectServer():
    def __init__(self, host, port):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.__client_socket.connect((host, port))
 
    def send_command(self, command):
        send_data = {'command': command}
        self.__client_socket.send(json.dumps(send_data).encode('utf_8'))

    def wait_response(self):
        data = self.__client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode("utf-8")
        print(raw_data)

        if raw_data == "closing":
            return False
        
        return True

if __name__ == '__main__':
    client = ConnectServer(host, port)

    keep_going = True
    while keep_going:
        command = input(">>>")
        client.send_command(command)
        keep_going = client.wait_response() 
    