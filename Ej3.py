#import process
from multiprocessing import Process, Lock
import time
import subprocess
import os

#create a class extends process
import psutil

class P1(Process):
	def __init__(self, name):
		super().__init__()
		self.name = name
	
	def run(self):
		subprocess.run(["gedit"])

	def getPid(self):
		return os.getpid()
	
	


class P2(Process):
	def __init__(self, name, pid1):
		super().__init__()
		self.name = name
		self.pid1 = pid1
	
	def run(self):
		print(self.pid1)
		time.sleep(5)
		for process in psutil.process_iter():
			if process.name() == "gedit":
				process.nice(10)
				break
		
	


class P3(Process):
	def __init__(self, name, pid1):
		super().__init__()
		self.name = name
		self.pid1 = pid1
		
	def run(self):
		print(self.pid1)
		for process in psutil.process_iter():
			if process.name() == "gedit":
				process.kill()
				break
	
	
	
p1 = P1("p1")
pid1= p1.getPid()


p1.start()
p2 = P2("p2", pid1)
p3 = P3("p3", pid1)

p2.start()

time.sleep(2)
p3.start()
