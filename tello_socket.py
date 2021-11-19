import socket
import time

drone1 = '10.10.4.144'
#drone2 = '192.168.137.17'

tello_port = 8889

#udpソケット
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone1_address = (drone1 , tello_port)
#drone2_address = (drone2 , tello_port)

#コマンドモードに入る
socket.sendto('command'.encode('utf-8'),drone1_address)
#socket.sendto('command'.encode('utf-8'),drone2_address)


time.sleep(3)

#離陸
socket.sendto('takeoff'.encode('utf-8'),drone1_address)
#socket.sendto('takeoff'.encode('utf-8'),drone2_address)

time.sleep(0.1)

#着陸
socket.sendto('land'.encode('utf-8'),drone1_address)
#socket.sendto('land'.encode('utf-8'),drone2_address)