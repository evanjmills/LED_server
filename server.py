import asyncio
import websockets
import board
import neopixel
import concurrent
import threading
import time
import adafruit_fancyled.adafruit_fancyled as fancy


def main():
    server = Server()
    server.start_server()

class Server:
    def __init__(self):
        self.run_preset = True
        self.preset_thread = None
        self.num_leds = 190
        self.pixels = neopixel.NeoPixel(board.D18, self.num_leds, brightness=0.1, auto_write=False)
        self.loop = asyncio.get_event_loop()

    def start_server(self):
        start_server = websockets.serve(self.set_lights, '192.168.0.132', 8080)

        self.loop = asyncio.new_event_loop()

        self.loop.run_until_complete(start_server)
        print('Started!\n')
        self.loop.run_forever()


    def restart(self):
<<<<<<< HEAD
<<<<<<< HEAD
        self.loop.stop()
        self.loop.close()
=======
=======
>>>>>>> parent of c580656... updated stuff
        asyncio.get_event_loop().run_until_complete(asyncio.get_event_loop().shutdown_asyncgens())
        asyncio.get_event_loop().stop()
        asyncio.get_event_loop().close()

<<<<<<< HEAD
>>>>>>> parent of c580656... updated stuff
=======
>>>>>>> parent of c580656... updated stuff
        start_server = websockets.serve(self.set_lights, '192.168.0.132', 8080)

        self.loop.run_until_complete(start_server)
        print('Started!\n')
        self.loop.run_forever()

    async def set_lights(self, websocket, path):
        try:
            code = await websocket.recv()
            print(f'Recieved: {code}')
            if code == 'p3':
                self.run_preset = True
                if self.preset_thread != None:
                    print(self.preset_thread.is_alive())
                self.preset_thread = threading.Thread(target=self.preset3, name='p3')
                
                self.preset_thread.start()
            else:
                self.run_preset = False
                rgb_values = code.split(',')
                for i, val in enumerate(rgb_values):
                    rgb_values[i] = int(val)

                self.pixels.fill((rgb_values[0], rgb_values[1], rgb_values[2]))
                self.pixels.show()

                response = f'The lights have been set to {code}'
                print(f'Sent: {response}')
                await websocket.send(response)
        except websockets.exceptions.ConnectionClosedOK:
            print('Server Closed')
            break
        except websockets.ConnectionClosedError:
            print('Restarting Server!\n')
            self.restart()

    def preset3(self):
        num_leds = 80

        # Declare a 6-element RGB rainbow palette
        palette = [
            fancy.CRGB(0.66, 0.0, 1.0),  # Green
            fancy.CRGB(0.0, 1.0, 1.0),  # Cyan
            fancy.CRGB(0.0, 0.75, 0.5),  # Blue
        ]  # Magenta

        offset = 0  # Positional offset into color palette to get it to 'spin'

        while self.run_preset:
            for i in range(num_leds):
                # Load each pixel's color from the palette using an offset, run it
                # through the gamma function, pack RGB value and assign to pixel.
                color = fancy.palette_lookup(palette, offset + i / num_leds)
                color = fancy.gamma_adjust(color, brightness=1.0)
                self.pixels[i] = color.pack()
            self.pixels.show()

            offset += 0.002  # Bigger number = faster spin


if __name__ == '__main__':
    print('Starting Server...')
    main()
