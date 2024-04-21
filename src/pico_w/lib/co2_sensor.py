
from machine import Pin
import utime
from machine import UART

def mesure_co2_value():
    uart = UART(1,baudrate=9600,tx=4,rx=5)
    uart.init(9600,bits=8, parity = None, stop=1)

    uart.write(b"\xFE\x44\x00\x08\x02\x9F\x25")
    utime.sleep_ms(3000)
    data = uart.read(7)
    #print(data)
    byte_3 = data[3]
    byte_4 = data[4]

    value = (byte_3*256)+byte_4    
    return(value)
