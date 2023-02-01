import utime
import pyb
class Encoder:
    
    def __init__ (self, in1pin, in2pin, timer, ch1, ch2):
        
        self.tim   = timer
        self.pin1  = in1pin
        self.pin2  = in2pin
        self.temp1 = 0
        self.count = 0
        self.ch1 = ch1
        self.ch2 = ch2
        
    def read(self):
        period=0xFFFF
        temp2 = self.tim.counter()
        #print(temp2)
        delta = temp2 - self.temp1
        self.temp1 = temp2
        if(delta > ((period + 1)/2)):
            delta -= period + 1
        elif(delta < (((-1 * period) + 1)/2)):
            delta += period + 1 
        self.count += delta
        #print(delta)
        print(self.count)
        
    def zero(self, count):
        #self.tim.counter() = 0
        count = 0
        return count 

if __name__ == '__main__':
    pinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    timer = pyb.Timer(4, prescaler=0, period=0xFFFF)
    
    ch1 = timer.channel (1, pyb.Timer.ENC_AB, pin=pinB6)
    ch2 = timer.channel (2, pyb.Timer.ENC_AB, pin=pinB7)
    
    encode = Encoder(pinB6,pinB7, timer, ch1, ch2)
    while (True):
        count = encode.read()
        utime.sleep(2)
        