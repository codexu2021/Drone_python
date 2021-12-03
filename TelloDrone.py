import socket
import subprocess
import sys


class DRONE():
    def __init__(self, macaddr):
        """intialize

        Args:
            macaddr (string): drone's mac address
        """
        self.macaddr = macaddr
        self.arp = subprocess.run(
            ["arp", "-a"], stdout=subprocess.PIPE, text=1)
        self.arp_list = self.arp.stdout.splitlines()

        for ip in self.arp_list:
            if (self.macaddr in ip):
                start = int(ip.find("(")) + 1
                end = int(ip.find(")"))
                self.ip = ip[start:end]
                print(f"[INFO] IPアドレス取得しました: {self.ip}")
        if self.ip is None:
            print("[INFO] IPアドレスが見つかりませんでした")
            print(self.arp_list)
            sys.exit()

        self.port = 8889
        self.drone = (self.ip, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.sendto("command".encode("utf-8"), self.drone)
        response, _ = self.socket.recvfrom(1024)
        print("from {}: {}".format(self.ip, response))

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
        # 危ないよ！ 緊急停止!
        print(self.__exec_command("emergency"))
