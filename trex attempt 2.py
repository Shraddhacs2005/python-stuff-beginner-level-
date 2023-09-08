import pyautogui
#play at https://trex-runner.com/
import time
time.sleep(3)
while True:
	mouseposition = pyautogui.position()
	if pyautogui.pixelMatchesColor(mouseposition[0], mouseposition[1],(83,83,83)):
		pyautogui.press('up')