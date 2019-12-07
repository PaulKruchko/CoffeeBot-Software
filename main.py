import pyb, micropython
from pyb import Pin, Timer, LED, Servo
import time
import encoderLib #for encoder
from Switch import Switch #for switch debounce
from DriveMotor import DriveMotor


# Exception buffer
micropython.alloc_emergency_exception_buf(100)

#Constants
ENCODER_SCALE = 1.257 #1.257 cm per tick of the encoder
FULL_LEFT = 45
FULL_RIGHT = -45
CENTER = 0
BACKUP_DISTANCE = 80 #cm

# Interface definitions and object instantiations

#Init drive motor
driveMotor = DriveMotor('X8', 'X21', 'X22', 1)
#Init steering servo
steerMtr = Servo(1)
#define LEDs
red_LED = LED(1)
grn_LED = LED(2)
#define USR switch for init main routine
strtSw = Switch('X17',50)
#define Switch class attributes for whiskers
leftWhisker = Switch('X19', 50)
rightWhisker = Switch('X20', 50)
# Initializes the library with pin CLK on X1
e = encoderLib.encoder('X11')
#will return current distance traveled in cm as it moves
last = 0
# define run flag
runFlg = 0

while True:
	
	if strtSw.getValue() and runFlg == 0:
            grn_LED.toggle()
            time.sleep_ms(500)
	
	else:
		runFlg = 1
		grn_LED.on()
	#encoder code
	#right now it just prints the distance traveled in cm
        irq_state = pyb.disable_irq() 
        encoderCnt = e.getValue()
        pyb.enable_irq(irq_state)
        if encoderCnt != last:
        	last = encoderCnt
                distance_cm = encoderCnt * ENCODER_SCALE
        	print(distance_cm)
            
	#loop for checking whisker values
	#right now will just print T for true if either goes low
        if leftWhisker.getValue() == 0:
            leftWhisker.wait_pin_change()
            leftCollision = True
            print('leftCollision = ',leftCollision)
        if rightWhisker.getValue() == 0:
            rightWhisker.wait_pin_change()
            rightCollision = True
            print('rightCollision = ',rightCollision)
    
        driveMotor.drive(10,'forward')
        
        if rightCollision or leftCollision == True:
            driveMotor.drive(0,'stop')
            reverseDist = distance_cm + BACKUP_DISTANCE
            
            if rightCollision == True:
                while distance_cm < reverseDist:
                    steerMtr.angle(FULL_RIGHT)
                    driveMotor.drive(10,'reverse')
                
                steerMtr.angle(CENTER)
                driveMotor.drive(10,'forward')
                
            if leftCollision == True:
                while distance_cm < reverseDist:
                    steerMtr.angle(FULL_LEFT)
                    driveMotor.drive(10,'reverse')
                
                steerMtr.angle(CENTER)
                driveMotor.drive(10,'forward')
                    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            