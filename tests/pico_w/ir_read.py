import utime
from machine import Pin
from machine import PWM

pin_in = Pin(15, Pin.IN, Pin.PULL_UP)
pin_out = Pin(16, mode=Pin.OUT)

HIGH_SIGNAL = int((2 ** 16) / 2)
LOW_SIGNAL = 0

#signels
fan = [10000000011111111101000000101111]
AC = [1000100011000000000001010001,1000100000000000110000001100]
# on,off

def send_code(pin, code, freq=38000):
    pwm = PWM(pin)
    pwm.freq(freq)

    # 9ms leading pulse
    pwm.duty_u16(HIGH_SIGNAL)
    utime.sleep_us(9000)

    # 4.5ms space
    pwm.duty_u16(LOW_SIGNAL)
    utime.sleep_us(4500)

    # for 0 - 562.5µs pulse + 562.5µs space, total 1.125ms
    # for 1 – 562.5µs pulse + 1.6875ms space, total 2.25ms
    for bit in code:
        pwm.duty_u16(HIGH_SIGNAL)
        utime.sleep_us(562)
        pwm.duty_u16(LOW_SIGNAL)
        utime.sleep_us(1687 if bit == "1" else 562)

    # End of message transmission - final 562.5µs pulse
    pwm.duty_u16(HIGH_SIGNAL)
    utime.sleep_us(562)
    pwm.duty_u16(LOW_SIGNAL)
    utime.sleep_us(562)

    pwm.deinit()


def read_code(pin):
    raw = []

    # Signal is inverted:
    # 0 - high signal
    # 1 - low signal

    # wait for the leading pulse
    while pin.value() == 1:
        pass

    # 9ms leading pulse
    # 4.5ms space
    utime.sleep_us(13500)

    # Sample signal every 562.5µs
    # Time sensitive
    for i in range(1000):
        raw.append(pin.value())
        utime.sleep_us(56)

    code = ""
    count = 0

    for sample in raw:
        if sample == 1:
            # count low signal
            count += 1
        else:
            # ignore high signal
            if count > 0:
                # if low signal is longer than 562.5µs it 1 otherwise 0
                code += "1" if count > 10 else "0"
                count = 0

    # trim message transmission and repeat codes
    return code[0:32]

class InvalidCodeException(Exception):
    pass


def validate_code(code):
    if len(code) < 32:
        raise InvalidCodeException

    if len(code) > 32:
        raise InvalidCodeException

    # check 8-bit device address
    # following 8-bits have to be a logical inverse of the device address
    for i in range(0, 8):
        if code[i] == code[i + 8]:
            raise InvalidCodeException

    # check 8-bit command
    # following 8-bits have to be a logical inverse of the command
    for i in range(16, 24):
        if code[i] == code[i + 8]:
            raise InvalidCodeException



while True: # main 

    print("sending.fan off >>> " )
    utime.sleep_ms(3000)
    send_code(pin_out, str(fan[0]))
    print(fan[0])
    utime.sleep_ms(3000)

    print("sending AC on >>> " )
    utime.sleep_ms(3000)
    send_code(pin_out, str(AC[1]))
    print(AC[1])

    utime.sleep_ms(600000)

    print("sending AC off >>> " )
    utime.sleep_ms(3000)
    send_code(pin_out, str(AC[0]))
    print(AC[0])

    utime.sleep_ms(60000)

    print("sending.fan on >>> " )
    utime.sleep_ms(3000)
    send_code(pin_out, str(fan[0]))
    print(fan[0])

    utime.sleep_ms(300000)



#while True:
#    out = read_code(pin_in)
#    # ignore random signals 
#    if out:
#        print("waiting to print")
#        utime.sleep_ms(20000)
#        send_code(pin_out, out)
#        print(out)
        #try:
        #    validate_code(out)
        #    print(out)
        #    utime.sleep(3)
        #    send_code(pin_out, out)
        #except InvalidCodeException:
        #    print("InvalidCodeException:" + out)

