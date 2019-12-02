import pyb
from Switch import Switch 

#define Switch class attributes for whiskers
leftWhisker = Switch('X19', 50)
rightWhisker = Switch('X20', 50)

#loop for checking whisker values
#right now will just print T for true if either goes low
while True:
	if leftWhisker.getValue() == 0:
		leftWhisker.wait_pin_change()
		print('T1')
	elif rightWhisker.getValue() == 0:
		rightWhisker.wait_pin_change()
		print('T2')

#ignore this for now its my non-working encoder example
#last = 0

# Initializes the library with pin on X1
#e = encoderLib.encoder('X1')

#while True:  # Infinite loop
#    value = e.getValue()  # Get rotary encoder value
#    if value != last:  # If there is a new value do
#        last = value
#        print(value)  # In this case it prints the value
