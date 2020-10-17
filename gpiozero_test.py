from gpiozero import LED, Button
from time import sleep
from signal import pause

led1 = LED(22)
led2 = LED(27)
led3 = LED(17)

def blink(led):
    print("I'm turning on the light")
    led.on()
    sleep(1)
    print("I'm turning off the light")
    led.off()
    sleep(1)
    blink(led)

# blink(led1)
# blink(led2)
# blink(led3)

button1 = Button(26)
button2 = Button(19)


def buttons(button, led):
    button.when_pressed = led.on if not led.is_lit else led.off
    

while True:
    buttons(button1, led1)
    buttons(button2, led2)


pause()

# dir(button)
# ['__attrs__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_active_event', '_active_state', '_check_open', '_conflicts_with', '_default_pin_factory', '_fire_activated', '_fire_deactivated', '_fire_events', '_fire_held', '_held_from', '_hold_repeat', '_hold_thread', '_hold_time', '_inactive_event', '_inactive_state', '_last_active', '_last_changed', '_pin', '_pin_changed', '_read', '_state_to_value', '_when_activated', '_when_deactivated', '_when_held', '_wrap_callback', 'active_time', 'close', 'closed', 'held_time', 'hold_repeat', 'hold_time', 'inactive_time', 'is_active', 'is_held', 'is_pressed', 'pin', 'pin_factory', 'pressed_time', 'pull_up', 'value', 'values', 'wait_for_active', 'wait_for_inactive', 'wait_for_press', 'wait_for_release', 'when_activated', 'when_deactivated', 'when_held', 'when_pressed', 'when_released']
# dir(led)
# ['__attrs__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_active_state', '_blink_device', '_blink_thread', '_check_open', '_conflicts_with', '_controller', '_copy_values', '_default_pin_factory', '_inactive_state', '_lock', '_pin', '_read', '_source', '_source_delay', '_source_thread', '_state_to_value', '_stop_blink', '_value_to_state', '_write', 'active_high', 'blink', 'close', 'closed', 'is_active', 'is_lit', 'off', 'on', 'pin', 'pin_factory', 'source', 'source_delay', 'toggle', 'value', 'values']

