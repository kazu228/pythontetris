from tkinter import *

win = Tk()
cv = Canvas(win, width=400, height=700, background="#000")
cv.pack()

data = [
    [1, 0],
    [1, 1],
    [0, 1]
]

# ブロックの一番最初のスタート位置
block_start_position_x = 200   
block_start_position_y = 10

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
    global block_start_position_x, block_start_position_y
    if not is_empty(data):
        #dataがあったとき、テトリスのブロック描画
        for d in data:
            for b in d:
                print(block_start_position_x)
                if b == 1: #dataが1、即ち、ブロックが存在する場合
                    # print('aaa')
                    cv.create_rectangle(block_start_position_x - block_size["x"], block_start_position_y - block_size["y"],
                                        block_start_position_x + block_size["x"], block_start_position_y + block_size["y"], fill="red")

                block_start_position_x += block_size["x"]

            block_start_position_x = 200
            block_start_position_y += block_size["y"]

def main(data):
    draw(data)

main(data)
win.mainloop()