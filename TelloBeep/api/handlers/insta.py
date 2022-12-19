from queue import Queue
import time, random, json, os, sys

from TelloBeep.api import Instagram_api

from instagrapi.exceptions import PleaseWaitFewMinutes, RateLimitError
from TelloBeep.config import conf
from TelloBeep.notify import Notify

#_____________________________________________________________
#
#               INSTAGRAM API
#_____________________________________________________________

class Insta_api():
	def __init__(self, q_list):
		
		
		print("instaapi")

		"this is only a makeshift"
		"fetching api function's going to replace this"

		self.q_list = q_list
		self.insta = Instagram_api(q_list=self.q_list)

		delay = 10
		while True:
			try:
				self.insta.login()
				break
			except PleaseWaitFewMinutes :
				Notify(q_list=self.q_list, error="PLEASE_WAIT_FEW_MINUTES")
				conf['logger'].warning(f"PLEASE_WAIT_FEW_MINUTES instagram login delay: {delay}")

				time.sleep(delay)
			except RateLimitError:
				Notify(q_list=self.q_list, error="RATE_LIMIT_ERROR")
				conf['logger'].warning(f"RATE_LIMIT_ERROR instagram login delay: {delay}")

				# time.sleep(delay)

			except Exception as e:
				print(e)
				Notify(q_list=self.q_list, error="INSTAGRAM_ERROR")
			
			time.sleep(delay)
			delay += 2 * delay





		self.recv_mgs()

	def recv_mgs(self) -> None:
		q = self.q_list.get("2insta")

		while 1 :
			content = q.get()
			# print(f"INSTAGRAM {content['title']}")

			path = f"{conf['out_image_path']}/{content['filename']}"

			if conf['CAPTION'] != "":
				pass
				self.insta.upload_post(path, caption=conf['CAPTION'])
			else:
				pass
				self.insta.upload_post(path)
			# print("instagram sent")

			time.sleep(0.1)