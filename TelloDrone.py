import socket
import subprocess
import sys


class DRONE():
    def __init__(self):
        """intialize

        Args: none
            first set up to controll drone 
        """
        self.command_port = 8889
        self.stat_port = 8890

    def battery_stat(self):
        drone_stat = (self.ip, self.stat_port)
        self.socket.sendto("battery?".encode("utf-8"),drone_stat)
        response, _ = self.socket.recvfrom(1024)
        print("バッテリー残量: {}%:".format(response))
        
    def __exec_command(self, command: str) -> str:
        try:
            self.socket.sendto(command.encode("utf-8"), self.drone)
            response, _ = self.socket.recvfrom(1024)
            if response == b"ok":
                return "[INFO] コマンドを実行しました -> send {} to {} res {}".format(
                    command, self.ip, response)
            else:
                if response in b"unknown command:":
                    return f"[INFO] コマンドの実行に失敗しました -> {command}というコマンドは存在しません。"
                else:
                    return f"[INFO] コマンドの実行に失敗しました -> {response}"
        except(KeyboardInterrupt):
            self.socket.sendto("land".encode("utf-8"), self.drone)
            response, _ = self.socket.recvfrom(1024)
            return "[INFO] 緊急着陸しました -> {}".format(
                response)
            
    def set_ip(self,macaddr):
        arp = subprocess.run(
            ["arp", "-a"], stdout=subprocess.PIPE, text=1)
        arp_list = arp.stdout.splitlines()

        for ip in arp_list:
            if (macaddr in ip):
                start = int(ip.find("(")) + 1
                end = int(ip.find(")"))
                self.ip = ip[start:end]
                print(f"[INFO] IPアドレス取得しました: {self.ip}")
        if ip is None:
            print("[INFO] IPアドレスが見つかりませんでした")
            print(arp_list)
            sys.exit()
            
        self.drone = (self.ip, self.command_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.sendto("command".encode("utf-8"), self.drone)
        response, _ = self.socket.recvfrom(1024)
        print("from {}: {}".format(self.ip, response))
            
    def get_ip(self):
        if self.ip ==None:
            print("set_ipを実行してね！")
        print(self.ip)

    def fly_test(self) -> str:
        """
        test mode to fly
        """
        commands = ["takeoff", "land"]
        for command in commands:
            print(self.__exec_command(command))

    def inline_exec(self, wait=True):
        """
        controll by terminal for single Tello
        """
        while(True):
            command = input("plz input command >>")
            if command == "exit" or "land":
                print(self.__exec_command("land"))
                sys.exit()
            print(self.__exec_command(command))
            # if wait = 1:

    def emergency_land(self):
        # 危ないよ！ 緊急停止! (急に落ちます)
        print(self.__exec_command("emergency"))
