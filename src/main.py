import utime
import lib 

pico_led = lib.digital_out(25)

# Flag to control whether the loop should continue running
running = True

def main_loop():
    while running:
        # Your main loop logic goes here
        pico_led.set_high()
        utime.sleep_ms(500)
        pico_led.set_low()
        utime.sleep_ms(500)
        
        
def stop():
    global running
    print("Stopping...")
    running = False

def start():
    global running
    print("Starting...")
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

