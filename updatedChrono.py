import time
import _thread
from tkinter import *



class chrono:
	hour = 0
	minute = 0
	second = 0
	pause = False
	

	def chrono(hour=0,minute=0,second=0):
		if chrono.pause == True:
			print("chrono paused")
		else:
			chrono.start(chrono.hour,chrono.minute,chrono.second)

				


	def start(hour=0, minute=0,second=0):
		
		state = 0
		prix = 500

		while state <= prix:
			if chrono.pause == True:
				break
			else:
				time.sleep(1)
				second += 1
				chrono.second = second

				if second == 60:
					minute += 1
					state += 30
					second = 0
					chrono.minute = minute
					if minute == 60:
						hour += 1
						chrono.hour = hour

				if state  > (prix-10):
					prix += 100

				print("{}:{}:{}".format(chrono.hour,chrono.minute,chrono.second))
				#print("le prix est: {} Ar \nle state {}".format(prix,state))


	def pauseChrono():
		chrono.pause = True
		print("Chronometer paused")

	def resumeChrono():
		chrono.pause = False
		print("Chronometer resumed")
		_thread.start_new_thread(chrono.chrono,())

	def interface():
		root = Tk()
		root.geometry("420x420")
		button = Button(root,text="pause", command= chrono.pauseChrono)
		button2 = Button(root, text="resume", command=chrono.resumeChrono)
		button.pack()
		button2.pack()
		root.mainloop()


_thread.start_new_thread(chrono.interface,())
_thread.start_new_thread(chrono.chrono,())
