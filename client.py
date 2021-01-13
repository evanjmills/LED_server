import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
from websocket import create_connection
import time
from threading import Thread

def main():
    uris = ['ws://192.168.0.103:8080', 'ws://192.168.0.104:8080', 'ws://192.168.0.105:8080', 'ws://192.168.0.132:8080', 'ws://192.168.0.144:8080', 'ws://192.168.0.145:8080', 'ws://192.168.0.146:8080', 'ws://192.168.0.147:8080', 'ws://192.168.0.148:8080']
    root = tk.Tk()
    root.geometry('500x500')
    app = Client(master=root, uris=uris)
    Thread(target=heartbeat, args=(uris,)).start()
    Thread(target=app.mainloop()).start()


def heartbeat(uris):
    while True:
        time.sleep(120)
        for uri in uris:
            connection = create_connection(uri)
            connection.send('Ping')
            connection.close


class Client(tk.Frame):
    def __init__(self, master=None, uris=None):
        super().__init__(master)
        self.uris = uris
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.p_3 = tk.Button(self.master, text='\nPreset 3\n', command=self.p3)
        self.p_3.pack(fill=tk.X, side="top")

        self.choose_color = tk.Button(self.master, text="\nChoose Color\n", command=self.choose)
        self.choose_color.pack(fill=tk.X, side="top")

        self.quit = tk.Button(self.master, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(fill=tk.X, side="bottom")

        self.off = tk.Button(self.master, text='\n Off\n', command=self.off)
        self.off.pack(fill=tk.X, side="bottom")

    def p3(self):
        self.send_code('p3')

    def choose(self):
        rgb = None

        temp = askcolor()[0]
        if temp != None:
            r = temp[0]
            g = temp[1]
            b = temp[2]            

            rgb = f'{r},{g},{b}'

            self.send_code(rgb)

    def off(self):
        rgb = '0,0,0'
        self.send_code(rgb)

    def send_code(self, code):
        for uri in self.uris:
            connection = create_connection(uri)
            connection.send(code)
            connection.close


if __name__ == '__main__':
    main()