from time import sleep
from random import randint

class Treater():
	def treat(self):
		print('Treating data...')
		print('Bip boop bop')
		secs = randint(1, 5)
		sleep(secs)
		print('Data has now cool features')
