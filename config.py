# Define HID Key Output Actions

from adafruit_hid.keycode import Keycode

hid_actions = [

    {
        "name": "Talk",
        "held": False,
        "keycode": (Keycode.COMMAND, Keycode.LEFT_SHIFT, Keycode.A, Keycode.CONTROL),
        "button": 1,
        "led": None,
    },
]
