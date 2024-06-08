print("Starting")

import board
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hidW

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP10, board.GP11,board.GP12,board.GP13) # Cols
keyboard.row_pins = (board.GP27, board.GP28,board.GP29)             # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
keyboard.keymap = [
    [KC.W, KC.A, KC.B, KC.C, KC.D, KC.E,KC.F, KC.G, KC.H, KC.J, KC.K, KC.L]
]

if __name__ == '__main__':
    keyboard.go()
