import socket
# unused drone ip: 144, 151
DRONE1_IPADDR = '10.10.4.145'
DRONE2_IPADDR = '10.10.4.146'
DRONE3_IPADDR = '10.10.4.147'
DRONE4_IPADDR = '10.10.4.148'
DRONE5_IPADDR = '10.10.4.149'
DRONE6_IPADDR = '10.10.4.152'

tello_port = 8889
drone1_address = (DRONE1_IPADDR, tello_port)
drone2_address = (DRONE2_IPADDR, tello_port)
drone3_address = (DRONE3_IPADDR, tello_port)
drone4_address = (DRONE4_IPADDR, tello_port)
drone5_address = (DRONE5_IPADDR, tello_port)
drone6_address = (DRONE6_IPADDR, tello_port)

drones = [
    drone1_address,
    drone2_address,
    drone3_address,
    drone4_address,
    drone5_address,
    drone6_address
    ]

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for drone in drones:
    socket.sendto('command'.encode('utf-8'), drone)
while(1):
    try:
        cmd = input("plz input command >> ")
        for drone in drones:
            socket.sendto(cmd.encode('utf-8'), drone)
    except KeyboardInterrupt:
        for drone in drones:
            socket.sendto("emergency".encode("utf-8"), drone)
    except Exception as e:
        print(e)