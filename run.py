#! /usr/bin/python3
from queue import Queue
from threading import Thread
import time, random, json

from make_img import Make_img
from backend.server import back_server

class Connect_api(object):
	def __init__(self, q_list):
		"this is only a makeshift"
		"fetching api function's going to replace this"
		self.q_list = q_list
		
		self.TEXT_tmp = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum """

		self.send_msg()

	def send_msg(self):
		while 1 :

			self.TEXT = self.TEXT_tmp[0: random.randrange(0, 1100)]
			
			q = q_list.get("2gen")
			
			t = time.localtime()
			y = f"{t.tm_year}"if len(str(t.tm_year)) == 4 else f"0{t.tm_year}"
			M = f"{t.tm_mon}" if len(str(t.tm_mon)) == 2 else f"0{t.tm_mon}"
			d = f"{t.tm_mday}"if len(str(t.tm_mday)) == 2 else f"0{t.tm_mday}"
			h = f"{t.tm_hour}"if len(str(t.tm_hour)) == 2 else f"0{t.tm_hour}"
			m = f"{t.tm_min}" if len(str(t.tm_min)) == 2 else f"0{t.tm_min}"
			s = f"{t.tm_sec}" if len(str(t.tm_sec)) == 2 else f"0{t.tm_sec}"

			title = f"{y}{M}{d}{h}{m}{s}"

			req = {
				"text": self.TEXT,
				"title": title
			}
			q.put(req)
			
			time.sleep(5)


if __name__ == "__main__":
	q_list = {
		"2gen": Queue(),
		"2flask": Queue(),
		"2api": Queue(),
	}

	
	
	#generating images
	t1 = Thread(target = Make_img, kwargs={"q_list":q_list}).start()

	#pushing text
	t2 = Thread(target = Connect_api, kwargs={"q_list":q_list}).start()
	
	#backend server
	t2 = Thread(target = back_server, kwargs={"q_list":q_list}).start()


	while 1 :		
		time.sleep(1)

