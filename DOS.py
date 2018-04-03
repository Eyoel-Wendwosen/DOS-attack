import urllib.request
import random
from threading import Thread
from time import sleep


def dosAttack():
	num1 = random.randrange(1,1000)
	num2 = random.randrange(1,1000)

	url = "http://localhost:4300/calculateRandom?num1=" + str(num1) + "&num2=" + str(num2)
	with urllib.request.urlopen(url) as f:
		print(f.read(300))


def threaded_function(arg):
    for i in range(1,5000):
    	dosAttack()
    	# sleep(1)


if __name__ == "__main__":
	for i in range(1,50):
		thread = Thread(target = threaded_function, args = (10, ))
		thread.start()
		# thread.run()
		
		# thread.join()
		print ("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nthread finished...exiting\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")