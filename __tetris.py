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
    colors = ["red", "blue", "yellow", "white", "green", "orange"]
    types = ["L", "I", "S", "O", "T"]

    # 配列のなかからランダムに選ぶ
    color_number = random.randint(0, len(colors)-1)
    type_number = random.randint(0, len(types)-1)

    block["color"] = colors[color_number]
    block["type"] = types[type_number]
    return block

def draw_l():
    cv.delete('all') 

    #L型ブロックの描画
    for i in range(4):
        cv.create_rectangle(block["x"] - block["w"], block["y"] - block["w"], 
                        block["x"] + block["w"], block["y"] + block["w"], fill=block["color"])
        if i == 3:
            block["x"] += block["w"] * 2  
            cv.create_rectangle(block["x"] - block["w"], block["y"] - block["w"], 
                                block["x"] + block["w"], block["y"] + block["w"], fill=block["color"])
            break
        block["y"] += block["w"] * 2

def draw_I():
    cv.delete('all')

    for i in range(4):
        cv.create_rectangle(block["x"] - block["w"], block["y"] - block["w"], 
                        block["x"] + block["w"], block["y"] + block["w"], fill=block["color"])

        block["y"] += block["w"] * 2

def draw_s():
    cv.delete('all')

    for k in range(2):
        for i in range(2):
            cv.create_rectangle(block["x"] - block["w"], block["y"] - block["w"], 
                        block["x"] + block["w"], block["y"] + block["w"], fill=block["color"])
            block["y"] += block["w"] * 2
        if k == 0:
            block["x"] += block["w"] * 2
            block["y"] -= block["w"] * 2


def main():
    create_data()
    block["type"] = "S"
    if block["type"] == "L":
        draw_l()
    if block["type"] == "I":
        draw_I()
    if block["type"] == "S":
        draw_s()
    

main()
win.mainloop()