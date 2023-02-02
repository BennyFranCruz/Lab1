import pyb

class MotorDriver:
    
    
    def __init__(self, en_pin, in1pin, in2pin, timer):
        
        self.tim   = timer
        self.enpin = en_pin
        self.pin1  = in1pin
        self.pin2  = in2pin
        
        
        self.enpin.value(0)
    
    
    def set_duty_cycle(self, level):
        
        ch1 = self.tim.channel (1, pyb.Timer.PWM, pin=self.pin1)
        ch2 = self.tim.channel (2, pyb.Timer.PWM, pin=self.pin2)
        
        if(level < 0):
            self.pin1 = ch1.pulse_width_percent(0)
            self.pin2 = ch2.pulse_width_percent(abs(level))
        elif(level > 0):
            self.pin1 = ch1.pulse_width_percent(abs(level))
            self.pin2 = ch2.pulse_width_percent(0)
        else:
            self.pin1 = ch1.pulse_width_percent(0)
            self.pin2 = ch2.pulse_width_percent(0)
        
        self.enpin.value(1)


if __name__ == '__main__':
    pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    timer = pyb.Timer (3, freq=10000)
    
    moe = MotorDriver(pinA10,pinB4,pinB5, timer)
    moe.set_duty_cycle (-20)

        