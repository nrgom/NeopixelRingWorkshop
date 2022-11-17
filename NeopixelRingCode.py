from machine import Pin
from neopixel import NeoPixel
import array, time



##########          SET UP I/O Pins & Variables          ##########
# Button Pin definitions
button_o = Pin(2, Pin.IN, Pin.PULL_UP)
button_y = Pin(3, Pin.IN, Pin.PULL_UP)
button_g = Pin(4, Pin.IN, Pin.PULL_UP)


# setup for neopixel ring
strip_pin = Pin(15, Pin.OUT)
num_pixels = 24
strip = NeoPixel(strip_pin, num_pixels)




##########          FUNCTION DEFINITIONS          ##########

# Checks button status
def get_button(button):
    status = not button.value()
    time.sleep(.1)
    return status

# Ring displays color 
def toggle_lights():
    color = (100,0,0) #red
    strip.fill(color)
    strip.write()

# Light goes around the ring
def LED_chase():
    color = (100,100,0) # yellow
    for i in range(0, num_pixels):
        strip.fill((0,0,0))
        strip[i] = color
        strip.write()
        time.sleep(0.1)
        
# Light fills the ring one LED at a time
def wheel_fill(wait):
    color = (0,100,0) # green
    for i in range(0, num_pixels):
        strip[i] = color
        strip.write()
        time.sleep(0.1)




##########          INFINITE LOOP          ##########
while True:
    if get_button(button_o) == 1:
        toggle_lights()
    elif get_button(button_y) == 1:
        LED_chase()
    elif get_button(button_g) == 1:
        wheel_fill(0.2)
    else:
        color = (0, 0, 0)
        strip.fill(color)
        strip.write()
        print("Push a button!")
