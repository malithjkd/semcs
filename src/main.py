import utime
import lib 



led_digital_out = lib.digital_out('WL_GPIO0')

# Flag to control whether the loop should continue running
running = True



def main_loop():
    while running:
        # Your main loop logic goes here
        led_digital_out.set_high()
        utime.sleep_ms(500)
        led_digital_out.set_low()
        utime.sleep_ms(500)
        
def stop():
    global running
    print("Stopping...")
    running = False

def start():
    global running
    print("Starting...")
    
    connect()
    
    running = True
    main_loop()

def main():
    start()

    # Main program loop to check for input to stop or restart the loop
    while True:
        utime.sleep(1)
        command = input("Enter 'stop' to stop the loop or 'start' to restart: ").strip().lower()
        if command == "stop":
            stop()
        elif command == "start":
            start()

if __name__ == "__main__":
    main()


