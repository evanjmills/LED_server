""" Simple FancyLED example for NeoPixel strip
"""

import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import sys

<<<<<<< HEAD
def preset3():
    num_leds = 50

    # Declare a 6-element RGB rainbow palette
    palette = [
        fancy.CRGB(1.0, 0.0, 0.0),  # Red
        fancy.CRGB(0.5, 0.5, 0.0),  # Yellow
        fancy.CRGB(0.0, 1.0, 0.0),  # Green
        fancy.CRGB(0.0, 0.5, 0.5),  # Cyan
        fancy.CRGB(0.0, 0.0, 1.0),  # Blue
        fancy.CRGB(0.5, 0.0, 0.5),
    ]  # Magenta

    # Declare a NeoPixel object on pin D6 with num_leds pixels, no auto-write.
    # Set brightness to max because we'll be using FancyLED's brightness control.
    pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=0.1, auto_write=False)
=======
num_leds = 50
if len(sys.argv) > 1:
	num_leds = int(sys.argv[1])

# Declare a 6-element RGB rainbow palette
palette = [
    fancy.CRGB(0.66, 0.0, 1.0),  # Red
    fancy.CRGB(0.0, 1.0, 1.0),  # Blue
    fancy.CRGB(0.0, 0.75, 0.5),
]  # Magenta

# Declare a NeoPixel object on pin D6 with num_leds pixels, no auto-write.
# Set brightness to max because we'll be using FancyLED's brightness control.
pixels = neopixel.NeoPixel(board.D18, num_leds, brightness=0.3, auto_write=False)
>>>>>>> ae680565a814dd9daf454ae5c6dd6ca88d686079

    offset = 0  # Positional offset into color palette to get it to 'spin'

<<<<<<< HEAD
    while True:
        for i in range(num_leds):
            # Load each pixel's color from the palette using an offset, run it
            # through the gamma function, pack RGB value and assign to pixel.
            color = fancy.palette_lookup(palette, offset + i / num_leds)
            color = fancy.gamma_adjust(color, brightness=0.25)
            pixels[i] = color.pack()
        pixels.show()
=======
while True:
    for i in range(num_leds):
        # Load each pixel's color from the palette using an offset, run it
        # through the gamma function, pack RGB value and assign to pixel.
        color = fancy.palette_lookup(palette, offset + i / num_leds)
        color = fancy.gamma_adjust(color, brightness=0.5)
        pixels[i] = color.pack()
    pixels.show()
>>>>>>> ae680565a814dd9daf454ae5c6dd6ca88d686079

        offset += 0.002  # Bigger number = faster spin
