import pyb
import encoderLib #for encoder
from Switch import Switch #for switch debounce

#define Switch class attributes for whiskers
leftWhisker = Switch('X19', 50)
rightWhisker = Switch('X20', 50)
# Initializes the library with pin CLK on X1
e = encoderLib.encoder('X1')
#will return current distance traveled in cm as it moves
last = 0

while True:
#encoder code
#right now it just prints the distance traveled in cm
	value = e.getValue()
    	if value != last:
        	last = value
        	print(value)
#loop for checking whisker values
#right now will just print T for true if either goes low
    	elif leftWhisker.getValue() == 0:
		leftWhisker.wait_pin_change()
		print('T1')
	elif rightWhisker.getValue() == 0:
		rightWhisker.wait_pin_change()
		print('T2')
