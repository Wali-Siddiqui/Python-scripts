#!/bin/usr/python
import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
            return
def main():
    ip = raw_input("[*] Enter the Target IP: ")
    for port in range(1,1000):
        banner = retBanner(ip,port)
        if banner:
            print "[+] " + str(ip) + " " + str(port) + " " + str(banner)
main()