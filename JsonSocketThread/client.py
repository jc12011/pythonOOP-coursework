# Python TCP Client A
import socket 
import sys
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class ConnectServer():
    def __init__(self, host, port):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket(ip_adress,port_num)
        #套接字格式：socket(family, type[,protocal]) 使用给定的套接族，套接字类型，协议编号（默认为0）来创建套接字
        #socket 类型	描述
        #socket.AF_UNIX	用于同一台机器上的进程通信（既本机通信）
        #socket.AF_INET	用于服务器与服务器之间的网络通信
        #socket.AF_INET6	基于IPV6方式的服务器与服务器之间的网络通信
        #socket.SOCK_STREAM	基于TCP的流式socket通信
        #socket.SOCK_DGRAM	基于UDP的数据报式socket通信
        #socket.SOCK_RAW	原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次SOCK_RAW也可以处理特殊的IPV4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头
        #socket.SOCK_SEQPACKET	可靠的连续数据包服务

        self.__client_socket.connect((host, port)) #tuple(host,port)
 
    def send_command(self, command):
        send_data = {'command': command}
        self.__client_socket.send(json.dumps(send_data).encode('utf_8')) 
        #send tcp data s.send(string[, flag]) 
        #s.send(string[,flag])
        #s为socket.socket()返回的套接字对象
        #string : 要发送的字符串数据 
        #flag : 提供有关消息的其他信息，通常可以忽略
        #返回值是要发送的字节数量，该数量可能小于string的字节大小。

    def wait_response(self):
        data = self.__client_socket.recv(BUFFER_SIZE)
        #s.recv(bufsize[, flag])	接受TCP套接字的数据，数据以字符串形式返回，buffsize指定要接受的最大数据量，flag提供有关消息的其他信息，通常可以忽略
        raw_data = data.decode("utf-8")
        print(raw_data)

if __name__ == '__main__':
    client = ConnectServer(host, port)

    command = sys.argv[1]
    client.send_command(command)
    client.wait_response() 
    