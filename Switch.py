import pyb
from pyb import Pin

#This is the debounce class for the input pins
class Switch():

    def __init__(self, pin, debouncePeriod):
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.db = debouncePeriod

    def getValue(self):
	return(self.pin.value())

    def wait_pin_change(self):
	# wait for pin to change value
	# it needs to be stable for a continuous 50ms
	cur_value = self.pin.value()
        active = 0
   	while active < self.db:
        	if self.pin.value() != cur_value:
         		active += 1
      		else:
         		active = 0
      		pyb.delay(1)