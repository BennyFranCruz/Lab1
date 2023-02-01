import pyb
import utime
import motor_driver

def INIT():
    #timer 4setup
    pinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    tim4 = pyb.Timer(4, prescaler=0, period=0xFFFF)
    
    #encoder
    ch1 = tim4.channel (1, pyb.Timer.ENC_AB, pin=pinB6)
    ch2 = tim4.channel (2, pyb.Timer.ENC_AB, pin=pinB7)
    return tim4
 
def main():
    temp1 = 0
    temp2 = 0
    count = 0
    delta = 0
    period = 0xFFFF
    tim4 = INIT()
    
    direction = 0
    up = 1
    
    #Motor Driver setup - timer 3
    
    
    pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    
    tim3 = pyb.Timer (3, freq=10000)
    ch1 = tim3.channel (1, pyb.Timer.PWM, pin=pinB4)
    ch2 = tim3.channel (2, pyb.Timer.PWM, pin=pinB5)
    
    pinB4 = ch1.pulse_width_percent(0)
    pinB5 = ch2.pulse_width_percent(50)
    
    pinA10.value(1)
    
    
    x = 0
    while(True):
        temp2 = tim4.counter()
        delta = temp2 - temp1
        temp1 = temp2
        if(delta > ((period + 1)/2)):
            delta -= period + 1
        elif(delta < (((-1 * period) + 1)/2)):
            delta += period + 1 
        count += delta
        print(count)

        
        try:
            while(x < 100):
                pinB5 = ch2.pulse_width_percent(x)
                x += 1
                utime.sleep(.05)
                print(x)
                
            while(x > 0):
                pinB5 = ch2.pulse_width_percent(x)
                x -= 1 
                utime.sleep(.05)
                print(x)
            
            while(x < 100):
                pinB4 = ch1.pulse_width_percent(x)
                x += 1
                utime.sleep(.05)
                print(x)
                
            while(x > 0):
                pinB4 = ch1.pulse_width_percent(x)
                x -= 1 
                utime.sleep(.05)
                print(x)
            
        except KeyboardInterrupt:
            break
        
if __name__ == "__main__":
    main()
        
    