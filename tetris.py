from tkinter import *

win = Tk()
cv = Canvas(win, width=400, height=700, background="#000")
cv.pack()

data = [
    [1, 0],
    [1, 1],
    [0, 1]
]

block_start_position_x, block_start_position_y = [200, 0]

block_size = {
    "x": 10,
    "y": 10
}

def is_empty(data):
    num = len(data)
    if num == 0:
        return True
    else:
        return False

def draw(data):
    if not is_empty(data):
        #dataがあったとき、テトリスのブロック描画
        for d in data:
            for b in d:
                if b == 1: #dataが1、即ち、ブロックが存在する場合
                    cv.create_rectangle()


win.mainloop()