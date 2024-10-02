import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

while True:
    print("Choose a color for the LEDs:")
    print("1: Red")
    print("2: Green")
    print("3: Blue")
    print("Press 'q' to quit")

    user_input = input("Enter your choice: ")

    if user_input == 'q':
        print("Goodbye!")
        break

    try:
        choice = int(user_input)

        if choice == 1:
            for i in range(10):
                cp.pixels[i] = (255, 0, 0)  # Red
            cp.pixels.show()
            print("LEDs are now red")
        elif choice == 2:
            for i in range(10):
                cp.pixels[i] = (0, 255, 0)  # Green
            cp.pixels.show()
            print("LEDs are now green")
        elif choice == 3:
            for i in range(10):
                cp.pixels[i] = (0, 0, 255)  # Blue
            cp.pixels.show()
            print("LEDs are now blue")
        else:
            print("Invalid choice, try again")
    
    except:
        print("Please enter a number or 'q' to quit.")


