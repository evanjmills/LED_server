import asyncio
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
from websocket import create_connection

def main():
    client = Client()
    client.run_client()
        

class Client:
    def __init__(self):
        self.ws = []

    def run_client(self):
        # while True:
        self.set_lights()

    def connect_websockets(self):
        uris = ['ws://192.168.0.132:8080', 'ws://192.168.0.144:8080', 'ws://192.168.0.145:8080', 'ws://192.168.0.146:8080', 'ws://192.168.0.147:8080', 'ws://192.168.0.148:8080']

        print('Connecting the websocket...')
        for uri in uris:
            try:
                temp = create_connection(uri)
                self.ws.append(temp)
            except Exception:
                continue
        
        print(f'Connected to: {self.ws}')

    def set_lights(self):
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

        self.connect_websockets()

        for web in self.ws:
            web.send(rgb)         
        
        for websocket in self.ws:
            websocket.close()


if __name__ == '__main__':
    main()

