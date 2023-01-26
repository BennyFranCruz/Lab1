import pyb
import utime

def INIT():
    pinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN_PP)
    pinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN_PP)
    tim4 = pyb.Timer(4, prescaler=0, period=0xFFFF)
    
    ch1 = tim4.channel (1, pyb.Timer.PWM, pin=pinB6)
    ch2 = tim4.channel (2, pyb.Timer.PWM, pin=pinB7)
    
    
    