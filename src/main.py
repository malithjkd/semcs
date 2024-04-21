import utime
import lib 



# Flag to control whether the loop should continue running
running = True

def main_loop():
    while running:
        # Your main loop logic goes here
        co2_value = lib.mesure_co2_value()
        humidity_value = lib.humidity_value()
        temparature_value = lib.temparature_value()
        print(co2_value, humidity_value,temparature_value)
        if co2_value < 400:
            lib.build_in_led(1)      
            utime.sleep_ms(150)
            lib.build_in_led(0)
            utime.sleep_ms(150)
        elif 400 <= co2_value <= 600:
            lib.switch_1(1)      
            utime.sleep_ms(150)
            lib.switch_1(0)
            utime.sleep_ms(150)
        elif 600 <= co2_value <= 800:
            lib.switch_2(1)      
            utime.sleep_ms(150)
            lib.switch_2(0)
            utime.sleep_ms(150)

        if humidity_value <= 50:
            lib.switch_3(1)      
            utime.sleep_ms(150)
            lib.switch_3(0)
            utime.sleep_ms(150)

        utime.sleep(3)
        
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

