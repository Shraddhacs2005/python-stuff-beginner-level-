import pyautogui as pg
import time
from pynput.mouse import Listener
from pynput.keyboard import Listener as ListenerKeyboard

# play at : http://tanksw.com/piano-tiles/
# Go to the code at the bottom. There are instructions. 

clickLocations = []
def on_click(x, y, button, pressed):
	if pressed:
		clickLocations.append([x, y])
		print("tileLocations = " + str(clickLocations))
		if len(clickLocations) >= 4:
			listener.stop()

def getTileLocationsOnScreen():
	pg.getTileLocationsOnScreen()
	# tileLocations = [[559, 302], [616, 289], [710, 287], [808, 281]]
with Listener(on_click=on_click) as listener:

		listener.join()

def on_click2(x, y, button, pressed):
	if pressed:
		print("blackTileColor = " + str(pg.pixel(x, y)))


def playGameClick(key):
	ListenerKeyboard(on_press=playGameClick).stop()
	print("Game Starts.")
	playGame2()
	

def playGame():
	 pg.playGame()
	 with ListenerKeyboard(on_press=playGameClick) as listener:
	 	listener.join()
       
	

def pickBlackTileColor():
	pg.pickBlackTileColor()
	# blackTileColor = (17, 17, 17)
with Listener(on_click=on_click2) as listener:

		listener.join()

tileKeys = ['a', 's', 'd', 'f']


def playGame2():
	while True:
		tileCount = 0
		for tileL in tileLocations:
			if pg.pixelMatchesColor(tileL[0], tileL[1], blackTileColor):
				pg.typewrite(tileKeys[tileCount])
			tileCount = tileCount + 1



# Record the locations of the four tiles using the function below. 
# Uncomment it. Make it a comment again once, you have used this function to find locations. Click in the correct order. A tile, S tile, D tile, F tile.

# getTileLocationsOnScreen()


# Copy paste the array/click location you get here, like the next line. There should be only four locations.
# tileLocations = [[802, 427], [932, 435], [1062, 426], [1180, 426]]

# Picks the color for the black tile. Just uncomment it. Click on a black tile. You'll get the color. 
# pickBlackTileColor()

# The color you got. Paste that color here. 
# blackTileColor = (17, 17, 17)

# Finally to start playing. Uncomment this. You will have to click for the first time, on the first tile, for the code to start. 
# playGame()
# code help credits : https://github.com/prajwalsouza :]


