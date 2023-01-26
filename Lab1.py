import pyb
import utime

def INIT():
    pinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    tim4 = pyb.Timer(4, prescaler=0, period=0xFFFF)
    
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
    while(True):
        try:
            temp2 = tim4.counter()
            delta = temp2 - temp1
            temp1 = temp2
            if(delta > ((period + 1)/2)):
                delta -= period + 1
            elif(delta < (((-1 * period) + 1)/2)):
                delta += period + 1 
            count += delta
            print(count)
            utime.sleep (.5)
            
        except KeyboardInterrupt:
            break
if __name__ == "__main__":
    main()
        
    