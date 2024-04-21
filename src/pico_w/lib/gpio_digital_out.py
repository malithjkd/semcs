import machine

def build_in_led(state):
    pico_led = machine.Pin("LED",machine.Pin.OUT)
    if state == 1:
        pico_led.value(1)
    else:
        pico_led.value(0)

def switch_1(state):
    gpio_13 = machine.Pin(13,machine.Pin.OUT)
    if state == 1:
        gpio_13.value(1)
    else:
        gpio_13.value(0)

def switch_2(state):
    gpio_14 = machine.Pin(14,machine.Pin.OUT)
    if state == 1:
        gpio_14.value(1)
    else:
        gpio_14.value(0)

def switch_3(state):
    gpio_15 = machine.Pin(15,machine.Pin.OUT)
    if state == 1:
        gpio_15.value(1)
    else:
        gpio_15.value(0)

