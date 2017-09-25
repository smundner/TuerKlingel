import socket

def main():
    br = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    br.bind(('192.168.0.137',60000))
    while(True):
        data,addr = br.recvfrom(1024)
        print(addr,data.decode())

if __name__ == '__main__':
    main()
