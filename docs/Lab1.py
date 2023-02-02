import pyb
import utime

import motor_driver
import encoder_reader

def main():
    #Encoder Stuff
    pinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    timer = pyb.Timer(4, prescaler=0, period=0xFFFF)
    
    ch1 = timer.channel (1, pyb.Timer.ENC_AB, pin=pinB6)
    ch2 = timer.channel (2, pyb.Timer.ENC_AB, pin=pinB7)
    
    encode = encoder_reader.Encoder(pinB6,pinB7, timer, ch1, ch2)
    encode.zero()
    
    #Motor Stuff
    pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    timer = pyb.Timer (3, freq=10000)
    
    moe = motor_driver.MotorDriver(pinA10,pinB4,pinB5, timer)
    
    moe.set_duty_cycle (-20)
    utime.sleep(2)
    moe.set_duty_cycle (50)
    utime.sleep(2)
    moe.set_duty_cycle (0)
    utime.sleep(2)
    
    while (True):
        count = encode.read()
        utime.sleep(.5)

    
if __name__ == "__main__":
    main()
        