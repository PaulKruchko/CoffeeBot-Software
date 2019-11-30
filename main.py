import pyb, time
from pyb import Pin

#function to debounce pin
def wait_pin_change(pin):
# wait for pin to change value
# it needs to be stable for a continuous 20ms
	cur_value = pin.value()
        active = 0
   	while active < 20:
        	if pin.value() != cur_value:
         		active += 1
      		else:
         		active = 0
      		pyb.delay(1)

#define pins for whiskers
leftWhisker = Pin('X19', Pin.IN, Pin.PULL_UP)
rightWhisker = Pin('X20', Pin.IN, Pin.PULL_UP)

#loop for checking pin values
while True:
	print('entered loop')
	print(wait_pin_change(leftWhisker).value())
	if wait_pin_change(leftWhisker).value() == 0 or wait_pin_change(rightWhisker).value() == 0:
		print('T')
	else:
		print('F')
