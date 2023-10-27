import os
import tkinter
import pathlib
from PIL import Image, ImageTk

res_dir = pathlib.Path("res")
WINDOW_SIZE = (1280, 720)

KEY_EVENT_TABLE = {}

class Sprite:
    def __init__(self, img_location, size=None):
        img_raw = Image.open(img_location)
        if size is None:
            img = img_raw
        else:
            img = img_raw.resize(size)
        img_tk = ImageTk.PhotoImage(img)
        self.label = tkinter.Label(image= img_tk)
        self.label.image = img_tk
    
    def place(self, coordinate):
        self.label.place(x=coordinate[0], y=coordinate[1])


class Mario:
    def __init__(self):
        self.location = []
        self.sprites = {}



if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

    main_background = Sprite(res_dir/"main-background.png", WINDOW_SIZE)
    main_background.place((0,0))

    window.mainloop()