class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        """
              
        self.in1pin = pyb.Pin(pyb.Pin.board.in1pin, pyb.Pin.OUT_PP)
        self.in2pin = pyb.Pin(pyb.Pin.board.in2pin, pyb.Pin.OUT_PP)
        self.enpin = pyb.Pin(pyb.Pin.board.en_pin, pyb.Pin.OUT_PP)
    
        self.timer = pyb.Timer (timer, freq=10000)
        
        timer.channel (1, pyb.Timer.PWM, pin=pinB4)
        timer.channel (2, pyb.Timer.PWM, pin=pinB5)
        
        print ("Creating a motor driver")

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
            
        #pinB4 = ch1.pulse_width_percent(0)
        #pinB5 = ch2.pulse_width_percent(50)
        print (f"Setting duty cycle to {level}")
        
if __name__ == "__main__":
        print("main")
    