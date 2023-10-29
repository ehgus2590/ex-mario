import os
import tkinter
import pathlib
from PIL import Image, ImageTk

res_dir = pathlib.Path("res")
WINDOW_SIZE = (1280, 720)

KEY_EVENT_TABLE = {}


class Unit:
    def __init__(self):
        self.position = ()
        self.label = tkinter.Label()
    
    def set_img(self, img, size= None):
        if size is not None:
            img = img.resize(size)
        self.label.configure(image=img)
        self.label.img = img
    
    def set_position(self, position):
        self.position = position
        self.label.place(x=position[0], y=position[1])

def load_sprite(img_location, size=None):
    img_raw = Image.open(img_location)
    if size is None:
        img = img_raw
    else:
        img = img_raw.resize(size)
    img_tk = ImageTk.PhotoImage(img)
    return img_tk


class Mario(Unit):
    def __init__(self):
        self.position = []
        self.sprites = {}

if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")    # 창 크기 설정
    window.resizable(False, False)    # 창 크기 조정 가능여부 설정 (가로, 세로)

    main_background = Unit()
    main_background.set_img(load_sprite(res_dir/"main-background.png", WINDOW_SIZE))
    main_background.set_position((0,0))


    window.mainloop()