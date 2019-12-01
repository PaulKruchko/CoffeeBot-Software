from pyb import Pin
from pyb import Timer

class encoder:
    # Init variables
    encoder_clk_prev = False
    i = 0

    def __init__(self, clk_pin):
        # Configure the rotary encoder pin and interrupt
        self.clk = Pin(clk_pin, Pin.IN, Pin.PULL_UP)

        tim = Timer(2)
        tim.init(  # Timer to run self.update every 5ms
            period = 5,
            callback = self.update
        )

    def getValue(self):
        return(self.i)  # Return rotary encoder value

    # Callback function
    def update(self, p):
        # Read the rotary encoder pins
        self.encoder_clk = self.clk.value()

        # If rotary encoder rotated
        if not self.encoder_clk and self.encoder_clk_prev:
 		if self.i < 20:
			self.i += 1
		else:
			self.i = 0

        self.encoder_clk_prev = self.encoder_clk
