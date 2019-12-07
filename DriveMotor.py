# Drive motor module
from pyb import Pin, Timer

class DriveMotor:

    def __init__(self, pwmPin, dirPin1, dirPin2,timerCh)
        self.pwmPin = Pin(pwmPin)
        self.dirPin1 = Pin(dirPin1, Pin.OUT_PP)
        self.dirPin2 = Pin(dirPin2, Pin.OUT_PP)
        self.channel = tim.channel(timerCh, Timer.PWM, self.pwmPin)
        
    def drive(self, dutyCycle, direction)
        if direction = 'forward':
            self.dirPin1.high()
            self.dirPin2.low()
        elif direction = 'reverse':
            self.dirPin1.low()
            self.dirPin2.high()
        elif direction = 'stop':
            self.dirPin1.low()
            self.dirPin2.low()
            
        self.pulse_width_percent(dutyCycle)
        