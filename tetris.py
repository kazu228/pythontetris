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
block_position_x = 200   
block_position_y = 10

block_size = {
    "x": 10,
    "y": 10
}

is_new_block = True

def is_empty(data):
    num = len(data)
    if num == 0:
        return True
    else:
        return False

def select_data():
    types = ["i", "j","l", "o", "s", "t", "z"]

    num = random.randint(0, len(types)-1)
    block_type = types[num]
    # block_type = "i"                   #仮で
    print(block_type)
    if block_type == "s":
        data = [
            [0, 0],
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
    if block_type == "j":
        data = [
            [0, 0],
            [0, 1],
            [0, 1],
            [1, 1]
        ]
    if block_type == "l":
        data = [
            [0, 0],
            [1, 0],
            [1, 0],
            [1, 1]
        ]
    if block_type == "o":
        data = [
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 1]
        ]
    if block_type == "t":
        data = [
            [0, 0],
            [1, 0],
            [1, 1],
            [1, 0]
        ]
    if block_type == "z":
        data = [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 0]
        ]
    return data

def draw(data):
    global block_position_x, block_position_y
    cv.delete('all')
    if not is_empty(data):
        is_new_block = False
        #dataがあったとき、テトリスのブロック描画
        for d in data:
            for b in d:
                if b == 1: #dataが1、即ち、ブロックが存在する場合
                    # print('aaa')
                    cv.create_rectangle(block_position_x - block_size["x"], block_position_y - block_size["y"],
                                        block_position_x + block_size["x"], block_position_y + block_size["y"], fill="red")

                # ブロックの幅分、ずらす。
                block_position_x += block_size["x"] * 2  

            block_position_x = 200
            # if block_position_y <= 600:
            block_position_y += block_size["y"] * 2     # ブロックの幅分、ずらす。

def move():
    #ブロックの下に進む先の座標
    global block_position_x, block_position_y, win
    if block_position_y <= 600:
        block_position_y += 10
    else:
        block_position_y = 640   # ゲームの底のy座標
        is_new_block = True
    
    win.bind("<Left>", key_event_left)
    win.bind("<Right>", key_event_right)

def key_event_left(e):
    global block_position_x
    if block_position_x > 0:
        block_position_x -= 10

def key_event_right(e):
    global block_position_x
    if block_position_x < 400:
        block_position_x += 10 
    

def main():
    if is_new_block:
        data = select_data()
    print(data)
    draw(data)
    move()
    win.after(1000, main)

main()
win.mainloop()