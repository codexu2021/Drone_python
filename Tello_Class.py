import time
import socket
import subprocess
import sys

class TelloDrone():
    def __init__(self, macAdress):
        '''
        config...
        '''
        self.macAdress = macAdress
        self.arp = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE, text=1)
        self.arp_list = self.arp.stdout.splitlines()
        
        for ip in self.arp_list:
            if (self.macAdress in ip):
                start = int(ip.find("(")) + 1
                end = int(ip.find(")"))
                self.ip = ip[start:end]
                print("OK")
        
        print(self.ip)
        self.port = 8889
        self.drone = (self.ip, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.start = self.socket.sendto('command'.encode('utf-8'), self.drone)
    
    def TestFly(self):
        self.start
        time.sleep(1)
        self.socket.sendto('takeoff'.encode('utf-8'), self.drone)
        time.sleep(3)
        self.socket.sendto('land'.encode('utf-8'), self.drone)
        print("飛行テスト")
    
    
    def CommandFly(self):  
        self.start

        while(1):
            command = input("plz input command >>")
            self.socket.sendto(command.encode('utf-8'), self.drone)
            time.sleep(2)
        
            
        

TelloDrone("34:d2:62:9f:19:48").CommandFly()
