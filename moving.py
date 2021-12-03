import threading
from TelloDrone import tellodrone


telloC = tellodrone("34:d2:62:9f:19:48")
#telloE = tellodrone("34:d2:62:9f:1b:4f")

command_list = ["takeoff", "forward 50", "cw 90", "forward 50", "land"]

telloC.CommandFly()


