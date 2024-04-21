from machine import Pin
import utime
import dht


def humidity_value():
    sensor = dht.DHT22(Pin(2))
    sensor.measure()
    return(sensor.humidity())

def temparature_value():
    sensor = dht.DHT22(Pin(2))
    sensor.measure()
    return(sensor.temperature())

