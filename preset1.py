import board
import neopixel
import sys

num_pixels = 80
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.10, auto_write=False)
color = sys.argv[1]

def shift_pixels():
	prevPixel = None
	for(i, pixel in enumerate(pixels)):
		prevPixel = pixel
		pixels[i] = prevPixel

	pixel[0] = prevPixel

def initPixels():
	count = 0
	toggle = True
	for(i in range(num_pixels)):
		count += 1
		if(count >= 8):
			toggle = False if toggle else True
			count = 0
		pixel[i] = 

while True:
	shift_pixels()
	pixels.show()
	time.sleep(0.1)
