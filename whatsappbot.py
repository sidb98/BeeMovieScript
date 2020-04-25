from pynput.keyboard import Key, Controller
import time 
keyboard = Controller()
time.sleep(5)
with open('beescript.txt','r') as f:
	for line in f:
		for word in line.split():
			for letters in word:
				keyboard.press(letters)
				keyboard.release(letters)
			keyboard.press(Key.space)
			keyboard.release(Key.space)
		time.sleep(1)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)