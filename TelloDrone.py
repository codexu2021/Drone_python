import time
import socket
import subprocess
import sys

class tellodrone():
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
                print("IPアドレス取得しました")
        
        
        print(self.ip)
        self.port = 8889
        self.drone = (self.ip, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.sendto('command'.encode('utf-8'), self.drone)
        self.response, ip = self.socket.recvfrom(1024)
        print('from {}: {}'.format(ip, self.response))
        
        """
        if (sys.argv[1] == True):
                file = sys.argv[1]
                with open(file) as f:
                    self.list = f.readlines()
                    print(self.list)
        """    
    def TestFly(self):
        '''
        test mode to fly
        '''
        time.sleep(1)
        self.socket.sendto('takeoff'.encode('utf-8'), self.drone)
        time.sleep(3)
        self.socket.sendto('land'.encode('utf-8'), self.drone)
        print("飛行テスト")
    
    
    def CommandFly(self,bool):  
        '''
        controll by terminal for single Tello
        '''
        try:
            while(1):
                command = input("plz input command >>")
                self.socket.sendto(command.encode('utf-8'), self.drone)
                self.response, ip = self.socket.recvfrom(1024)
                if bool == 1:
                    print('from {}: {}'.format(ip, self.response))
                    
        except KeyboardInterrupt:
            print("緊急着陸します")
            self.socket.sendto("land".encode("utf-8"), self.drone)
            sys.exit()
        except Exception as e:
            print(e)
            self.socket.sendto("land".encode("utf-8"), self.drone)
            print("停止します")
            sys.exit()
            
    def CommandMode(self, commands):
        '''to controll for multi tello'''
        try:
            for command in commands:
                self.socket.sendto(command.encode('utf-8'), self.drone)
                self.response, ip= self.socket.recvfrom(1024)
                print('from {}: {}'.format(ip, self.response))
        except(KeyboardInterrupt):
            print("緊急着陸します")
            self.socket.sendto("land".encode("utf-8"), self.drone)
            sys.exit()
        

