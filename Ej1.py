import time
import threading
import random
import queue as Queue

class Producer(threading.Thread):

	def __init__(self, queue, pt):

		threading.Thread.__init__(self)
		self.queue = queue
		self.pt=pt

	def run(self):
		while True:
			print("Producer thread for queue")
			self.queue.put(random.randint(100, 500)) 
			print(list(self.queue.queue))  
			time.sleep(self.pt) # PT producer time


class Consumer(threading.Thread):
	"""
	Consumes random integers from a list
	"""

	def __init__(self, queue, ct, x):
		threading.Thread.__init__(self)
		self.queue = queue
		self.ct=ct
		self.x=x
	
	def run(self):
		while True:
			list = []
			for i in range(self.x):  
				list.append(self.queue.get())
			
			solution = 1
			for i in list:
				solution *= i
			print(solution)

			time.sleep(self.ct)  # CT consumer time
	
 
def mainEj(nP,nC,pt,ct,X):
	integers = []
	queue = Queue.Queue()
	listProducer = []
	for i in range(nP):
		t1 = Producer(queue, pt)
		listProducer.append(t1)

	listConsumer = []
	for i in range(nC):
		t2 = Consumer(queue,ct,X)
		listConsumer.append(t2)

	for i in listProducer:
		i.start()
		
	for i in listConsumer:
		i.start()
	
	for i in listProducer:
		i.join()

	for i in listConsumer:
		i.join() 				  


mainEj(2,1,1,4,3)
mainEj(4,2,2,2,2)
mainEj(2,5,1,10,4)