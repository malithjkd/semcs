import machine


class digital_out():

    def __init__(self,pin_number):
        self.pin = machine.Pin(pin_number,machine.Pin.OUT)


    def set_high(self):
        self.pin.value(1)

    def set_low(self):
        self.pin.value(0)
    
    def set_out(self, state):
        self.pin.value(state)
