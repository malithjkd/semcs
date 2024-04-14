
import utime

# Flag to control whether the loop should continue running
running = True

def main_loop():
    while running:
        # Your main loop logic goes here
        print("Running...")
        utime.sleep(2)

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
        command = input("Enter 'stop' to stop the loop or 'start' to restart: ").strip().lower()
        if command == "stop":
            stop()
        elif command == "start":
            start()

if __name__ == "__main__":
    main()