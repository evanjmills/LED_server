import asyncio
import websockets
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor

def main():
    client = Client()
    client.run_client()
        

class Client:
    def __init__(self):
        self.ws = []

    def run_client(self):
        print('Connecting to servers')
        asyncio.get_event_loop().run_until_complete(self.connect_websockets())
        print(f'Connected to: {self.ws}')
        while True:
            asyncio.get_event_loop().run_until_complete(self.set_lights())

    async def connect_websockets(self):
        uris = ['ws://192.168.0.132:8080', 'ws://192.168.0.145:8080', 'ws://192.168.0.146:8080']

        print('Connecting the websocket...')
        for uri in uris:
            try:
                temp = await websockets.connect(uri)
                self.ws.append(temp)
            except Exception:
                continue

    async def set_lights(self):
        try:
            root = tk.Tk()
            style = ttk.Style(root)
            style.theme_use('clam')

            rgb = None

            temp = askcolor()[0]
            if temp == None:
                rgb = 'p3'
            else:
                r = temp[0]
                g = temp[1]
                b = temp[2]

                rgb = f'{r},{g},{b}'

            root.destroy()

            for websocket in self.ws:
                await websocket.send(rgb)         
            
        except websockets.exceptions.ConnectionClosed:
            self.connect_websockets()
            

if __name__ == '__main__':
    main()

