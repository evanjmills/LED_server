import asyncio
import websockets
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 190, brightness=0.80, auto_write=False)

async def set_lights(websocket, path):
    while True:
        try:
            rgb = await websocket.recv()
            print(f'Recieved: {rgb}')

            rgb_values = rgb.split(',')
            for i, val in enumerate(rgb_values):
                rgb_values[i] = int(val)

            pixels.fill((rgb_values[0], rgb_values[1], rgb_values[2]))
            pixels.show()

            response = f'The lights have been set to {rgb}'
            print(f'Sent: {response}')
            await websocket.send(response)
        except websockets.exceptions.ConnectionClosedOK:
            print('Server Closed')
            break


if __name__ == '__main__':
    print('Starting Server...')
    start_server = websockets.serve(set_lights, '192.168.0.146', 8080)

    asyncio.get_event_loop().run_until_complete(start_server)
    print('Started!\n')
    asyncio.get_event_loop().run_forever()
