import machine

class digital_out:
    def __init__(self,pin_number):
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)

    def set_high(self):
        self.pin.value(1)

    def set_low(self):
        self.pin.value()



#def switch_1(state):
#    gpio_13 = machine.Pin(13,machine.Pin.OUT)
#    if state == 1:
#        gpio_13.value(1)
#    else:
#        gpio_13.value(0)
#
#def switch_2(state):
#    gpio_14 = machine.Pin(14,machine.Pin.OUT)
#    if state == 1:
#        gpio_14.value(1)
#    else:
#        gpio_14.value(0)
#
#def switch_3(state):
#    gpio_15 = machine.Pin(15,machine.Pin.OUT)
#    if state == 1:
#        gpio_15.value(1)
#    else:
#        gpio_15.value(0)
#
