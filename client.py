import asyncio
import websockets

async def set_lights():
    uri = 'ws://192.168.0.132:8080'

    print('Connecting the websocket...')

    async with websockets.connect(uri) as websocket:
        while True:
            try:
                print('Connected!\n')
                r = -1
                g = -1
                b = -1
                while r not in range(0, 256):
                    r = int(input('Red Value: '))
                while g not in range(0, 256):
                    g = int(input('Green Value: '))
                while b not in range(0, 256):
                    b = int(input('Blue Value: '))

                rgb = f'{r},{g},{b}'

                await websocket.send(rgb)
                print(f'Sent: {rgb}')

                response = await websocket.recv()
                print(f'Recieved: {response}')
            except websockets.exceptions.ConnectionClosed:
                break
            

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(set_lights())
    print('Client Started')
    asyncio.get_event_loop().run_forever()
