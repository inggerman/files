#!/bin/bash

# Connect to WiFi
sudo nmtui

# Update package list
sudo apt update

# Install pip3
sudo apt install python3-pip -y

# Install OrangePi.GPIO library
sudo pip3 install OrangePi.GPIO

# Create Python script for arcade buttons
echo 'import OrangePi.GPIO as GPIO
import time

# Configure GPIO
GPIO.setmode(GPIO.BOARD)

# Configure pins for Player 1
buttons_j1 = [11, 12, 13, 15, 16, 18, 22, 7]
joystick_j1 = [29, 31, 33, 35]
for pin in buttons_j1 + joystick_j1:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configure pins for Player 2
buttons_j2 = [36, 37, 38, 40, 32, 26, 24, 21]
joystick_j2 = [19, 23, 8, 10]
for pin in buttons_j2 + joystick_j2:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read buttons for Player 1
        for pin in buttons_j1:
            if GPIO.input(pin) == False:
                print(f"Player 1 pressed the button on pin {pin}")

        # Read joystick for Player 1
        for pin in joystick_j1:
            if GPIO.input(pin) == False:
                print(f"Player 1 moved the joystick on pin {pin}")

        # Read buttons for Player 2
        for pin in buttons_j2:
            if GPIO.input(pin) == False:
                print(f"Player 2 pressed the button on pin {pin}")

        # Read joystick for Player 2
        for pin in joystick_j2:
            if GPIO.input(pin) == False:
                print(f"Player 2 moved the joystick on pin {pin}")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()' > arcade_buttons.py

# Make the Python script executable
chmod +x arcade_buttons.py

# Run the Python script
python3 arcade_buttons.py
