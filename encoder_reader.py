import utime
import pyb

class Encoder:
    
    def __init__ (self, in1pin, in2pin, timer, ch1, ch2):
        #add in correct documentation
        
        self.tim   = timer
        self.pin1  = in1pin
        self.pin2  = in2pin
        self.temp1 = 0
        self.position = 0
        self.ch1 = ch1
        self.ch2 = ch2
        
    def read(self):
        period=0xFFFF
        temp2 = self.tim.counter()
        delta = temp2 - self.temp1
        self.temp1 = temp2
        if(delta > ((period + 1)/2)):
            delta -= period + 1
        elif(delta < (((-1 * period) + 1)/2)):
            delta += period + 1 
        self.position += delta
        #print(delta)
        print(self.position)
        
    def zero(self):
        self.position = 0
      