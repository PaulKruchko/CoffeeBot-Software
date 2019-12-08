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
FULL_LEFT = 30
FULL_RIGHT = -30
CENTER = 0
BACKUP_DISTANCE = 80 #cm

# Interface definitions and object instantiations

#Init drive motor
driveMotor = DriveMotor('X8', 'X21', 'X22', 14, 1)
driveMotor.drive(0,'stop')
#Init steering servo
steerMtr = Servo(1)
#define LEDs
red_LED = LED(1)
grn_LED = LED(2)
#define USR switch for init main routine
strtSw = Switch('X17',1)
#define Switch class attributes for whiskers
leftWhisker = Switch('X19', 20)
rightWhisker = Switch('X20', 20)
# Initializes the library with pin CLK on X1
e = encoderLib.encoder('X11')
#Init bools
rightCollision = False
leftCollision = False
colFlag = False
strtRun = False
backUpRight = False
backUpLeft = False

#will return current distance traveled in cm as it moves
last = 0
# define run flag
runFlg = 0

while True:
    
    irq_state = pyb.disable_irq()
    strtSwState = strtSw.getValue()
    pyb.enable_irq(irq_state)
    
    # States and modes
    if strtSwState == 0:
        strtRun = True
        print('Run State = ',strtRun)
        
    elif strtRun == False and runFlg == 0:
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
        else:
            pass
    #Collision detection
        irq_state = pyb.disable_irq() 
        if leftWhisker.getValue() == 0:
            leftWhisker.wait_pin_change()
            leftCollision = True
            print('leftCollision = ',leftCollision)
        else:
            leftCollision = False
        pyb.enable_irq(irq_state)
        
        irq_state = pyb.disable_irq() 
        if rightWhisker.getValue() == 0:
            rightWhisker.wait_pin_change()
            rightCollision = True
            print('rightCollision = ',rightCollision)
        else:
            rightCollision = False
        pyb.enable_irq(irq_state)  
            
    # Collision interdiction
   
        if rightCollision or leftCollision == True:
            irq_state = pyb.disable_irq() 
            driveMotor.drive(0,'stop')
            e.update(0)
            distance_cm = 0.0
            pyb.enable_irq(irq_state)
            print(e.getValue())
            
            if rightCollision == True:
                backUpRight = True
                
            elif leftCollision == True:
                backUpLeft = True
        else:
            pass
        
        if backUpRight == True:
            print(distance_cm)
            if distance_cm < BACKUP_DISTANCE:
                irq_state = pyb.disable_irq()
                steerMtr.angle(FULL_RIGHT)
                driveMotor.drive(50,'reverse')
                pyb.enable_irq(irq_state)
                print(steerMtr.pulse_width())
            else:
                irq_state = pyb.disable_irq()
                backUpRight = False
                steerMtr.angle(CENTER)
                driveMotor.drive(50,'forward')
                pyb.enable_irq(irq_state) 
                
        elif backUpLeft == True:
            print(distance_cm)
            if distance_cm < BACKUP_DISTANCE:
               irq_state = pyb.disable_irq()
               steerMtr.angle(FULL_LEFT)
               driveMotor.drive(50,'reverse')
               pyb.enable_irq(irq_state)
               print(steerMtr.pulse_width())
            else:
                irq_state = pyb.disable_irq()
                backUpLeft = False
                steerMtr.angle(CENTER)
                driveMotor.drive(50,'forward')
                pyb.enable_irq(irq_state) 
        else:
            irq_state = pyb.disable_irq()
            steerMtr.angle(CENTER)
            driveMotor.drive(50,'forward')
            pyb.enable_irq(irq_state) 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            