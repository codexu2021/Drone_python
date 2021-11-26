import socket

DRONE1_IPADDR = '10.10.4.144'
DRONE2_IPADDR = '10.10.4.151'
DRONE3_IPADDR =  '10.10.4.149'

tello_port = 8889

drone1_address = (DRONE1_IPADDR, tello_port)
drone2_address = (DRONE2_IPADDR, tello_port)
drone3_address = (DRONE3_IPADDR, tello_port)

drones = [
    drone1_address,
    drone2_address,
    drone3_address,
]

a  =True
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for drone in drones :
    socket.sendto('command'.encode('utf-8'), drone)
while(a):
    try:
        for drones in drone:
            command = input("コマンドを入力してね >> ")
            socket.sendto(command.encode('utf-8'),drone)
    except KeyboardInterrupt:
        for drones in drone:
            socket.sendto("land".encode("utf-8"), drone)
        break
    except Exception as e:
        print(e)
