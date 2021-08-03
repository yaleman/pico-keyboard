import time
import usb_hid
import board

from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize Keybaord
keyboard = Keyboard(usb_hid.devices)

from config import hid_actions


# Define button pins
btn_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
]

# Define led pins
led_pins = [
    board.GP13,
    board.GP14,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    board.GP27,
    board.GP28,
]

for action in hid_actions:
    if action.get('button'):
        button = DigitalInOut(btn_pins[action.get('button')])
        button.direction = Direction.INPUT
        button.pull = Pull.UP
        action['button'] = button
        action['registered'] = True

        print(f"Registering: {action}")
    else:
        action['registered'] = False



registered_actions = [ action for action in hid_actions if action.get('registered')]

def is_pressed(action):
    """ inverts the button thing to return a 'pressed' value """
    return not action['button'].value

# Loop around and check for key presses
while True:
    for action in registered_actions:
        # print(action)
        if is_pressed(action) and not action.get('held'):
            # for key in action.get('keycode'):
            keyboard.press(*action.get('keycode'))
            print(f"Action {action.get('name')} pressed")
        elif not is_pressed(action) and action.get('held'):
            for key in action.get('keycode'):
                keyboard.release(key)
            print(f"Action {action.get('name')} released")
        action['held'] = is_pressed(action)

