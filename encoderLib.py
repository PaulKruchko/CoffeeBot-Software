from pyb import Pin
from machine import Timer

class encoder:
    # Init variables
    encoder_clk_prev = False
    i = 0

    def __init__(self, clk_pin):
        # Configure the rotary encoder pins and interrupt
        self.clk = Pin(clk_pin, Pin.IN, Pin.PULL_UP)

        tim = Timer(-1)
        tim.init(  # Timer to run self.update every 5ms
            period=5,
            mode=Timer.PERIODIC,
            callback=self.update
        )

    def getValue(self):
        return(self.i)  # Return rotary encoder value

    # Non blocking delay of 5ms
    def update(self, p):
        # Read the rotary encoder pins
        self.encoder_clk = self.clk.value()
        if not self.encoder_clk and self.encoder_clk_prev:
            self.i += 1
            
        self.encoder_clk_prev = self.encoder_clk
