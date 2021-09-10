from tkinter import *
import random


win = Tk()
cv = Canvas(win, width=400, height=700, background="#000")
cv.pack()

# data = [
#     [1, 0],
#     [1, 1],
#     [0, 1]
# ]

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

def select_data():
    types = ["i", "j", "k", "l", "o", "s", "t", "z"]

    num = random.randint(0, len(types))

    block_type = types[num]
    block_type = "i"

    if block_type == "s":
        data = [
            [1, 0],
            [1, 1],
            [0, 1]
        ]
    if block_type == "i":
        data = [
            [0, 1],
            [0, 1],
            [0, 1],
            [0, 1]
        ]
    return data

def draw(data):
    global block_start_position_x, block_start_position_y
    if not is_empty(data):
        #dataがあったとき、テトリスのブロック描画
        for d in data:
            for b in d:
                if b == 1: #dataが1、即ち、ブロックが存在する場合
                    # print('aaa')
                    cv.create_rectangle(block_start_position_x - block_size["x"], block_start_position_y - block_size["y"],
                                        block_start_position_x + block_size["x"], block_start_position_y + block_size["y"], fill="red")

                # ブロックの幅分、ずらす。
                block_start_position_x += block_size["x"] * 2  

            block_start_position_x = 200
            block_start_position_y += block_size["y"] * 2     # ブロックの幅分、ずらす。

def main():
    data2 = select_data()
    print(data2)
    draw(data2)

main()
win.mainloop()