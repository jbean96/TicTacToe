import sys
import time
import random

def print_typing(string, end="\n", base_delay=0.02):
	for char in string:
		sys.stdout.write(char)
		sys.stdout.flush()
		delay = base_delay + float("0.0" + str(random.randint(0, 5)))
		delay = float(delay)
		time.sleep(delay)
	sys.stdout.write(end)