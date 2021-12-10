from TelloDrone import DRONE


telloA = DRONE()
#telloB = DRONE()
telloA.set_ip("macaddr")
#telloB.set_ip("macaddr")
telloA.get_ip()
telloA.battery_stat()
# macアドレスを入力

telloA.fly_test()

import threading

#2台を並列処理
#threadA = threading.Thread(target=telloA.fly_test)
#threadB = threading.Thread(target=telloB.fly_test)
#threadA.start()
#threadB.start()
#threadA.join()
#threadB.join()
#print("テスト飛行の終了")
