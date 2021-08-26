from tkinter import *
import random

block = {
    "color": "red",
    "x": 5,
    "y": 5,
    "w": 15,
    "type": "L"
}

win = Tk()
cv = Canvas(win, width=400, height=700, background="#000")
cv.pack()

def create_data():
    colors = ["red", "blue", "yellow", "white", "black", "green", "orange"]
    types = ["L", "I", "S", "O", "T"]

    # 配列のなかからランダムに選ぶ
    color_number = random.randint(0, len(colors)-1)
    type_number = random.randint(0, len(types)-1)

    block["color"] = colors[color_number]
    block["type"] = types[type_number]
    return block

def draw():
    cv.delete('all') 

    #ブロックの描画
    cv.create_rectangle(block["x"] - block["w"], block["y"] - block["w"], 
                        block["x"] + block["w"], block["y"] + block["w"], fill=block["color"])

def main():
    create_data()
    draw()

main()
win.mainloop()