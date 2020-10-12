from gpiozero import LED
from time import sleep

led = LED(2)

while True:
    print("I'm turning on the light")
    led.on()
    sleep(1)
    print("I'm turning off the light")
    led.off()
    sleep(1)

