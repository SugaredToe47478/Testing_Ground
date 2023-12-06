# Import the RPi.GPIO library
import RPi.GPIO as GPIO
# Import the time library
import time

# Set the GPIO mode to BOARD
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for the servo and the ESC
SERVO_PIN = 11
ESC_PIN = 13

# Set the servo and ESC pins as output
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(ESC_PIN, GPIO.OUT)

# Create PWM objects for the servo and ESC with 50 Hz frequency
servo = GPIO.PWM(SERVO_PIN, 50)
esc = GPIO.PWM(ESC_PIN, 50)

# Start the PWM with 0% duty cycle (no signal)
servo.start(0)
esc.start(0)

# Define a function to map the angle to the duty cycle
def angle_to_duty(angle):
    # The duty cycle ranges from 2.5% to 12.5% for 0 to 180 degrees
    return 2.5 + (angle / 180) * 10

# Define a function to map the speed to the duty cycle
def speed_to_duty(speed):
    # The duty cycle ranges from 5% to 10% for 0 to 100% speed
    return 5 + (speed / 100) * 5

# Move the servo to 90 degrees
servo.ChangeDutyCycle(angle_to_duty(90))

# Set the ESC speed to 50%
esc.ChangeDutyCycle(speed_to_duty(50))

# Pause for 5 seconds
time.sleep(5)

# Stop the PWM
servo.stop()
esc.stop()

# Clean up the GPIO
GPIO.cleanup()
