import asyncio
import websockets
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor

def main():
    asyncio.get_event_loop().run_until_complete(set_lights())
    print('Client Started')
    asyncio.get_event_loop().run_forever()
        

async def set_lights():
    uri = 'ws://192.168.0.132:8080'

    print('Connecting the websocket...')

    async with websockets.connect(uri) as websocket:
        while True:
            try:
                root = tk.Tk()
                style = ttk.Style(root)
                style.theme_use('clam')

                temp = askcolor()[0]
                r = temp[0]
                g = temp[1]
                b = temp[2]
                root.destroy()

                rgb = f'{r},{g},{b}'

                await websocket.send(rgb)
                print(f'Sent: {rgb}')

                response = await websocket.recv()
                print(f'Recieved: {response}')
            except websockets.exceptions.ConnectionClosed:
                break
            

if __name__ == '__main__':
    main()

