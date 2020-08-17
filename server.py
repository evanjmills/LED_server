import asyncio
import websockets
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

async def set_lights(websocket, path):
    rgb = await websocket.recv()
    print(f'Recieved: {rgb}')

    rgb_values = rgb.split(',')
    for i, val in enumerate(rgb_values):
        rgb_values[i] = int(val)

    print(rgb_values)

    response = f'The lights have been set to {rgb}'
    print(f'Sent: {response}')
    await websocket.send(response)


if __name__ == '__main__':
    print('Starting Server...')
    start_server = websockets.serve(set_lights, 'localhost', 8080)

    asyncio.get_event_loop().run_until_complete(start_server)
    print('Started!\n')
    asyncio.get_event_loop().run_forever()