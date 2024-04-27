from machine import Pin
import utime
import network
import machine

ssid = 'NinjaWarriers'
password = 'Boys1234'

# Connect to network
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    utime.sleep_ms(1000)
    for x in range(1,50):
        if wlan.isconnected() == False:
            print('Waiting for connection...')
            utime.sleep_ms(1000)
        else:
            ip = wlan.ifconfig()[0]
            print(f'Connected on {ip}')
            break
        x = x+1
