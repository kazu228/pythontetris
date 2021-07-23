from tkinter import *
from random import randint as rnd
import tkinter.messagebox as msgbox

data = {
    vertical = 20     #基盤の縦のマス数
    side = 10     #基盤の横のマス数
    size = 30     #1マスの大きさ
    mino_size = 4    #ミノの(縦横最大の)ブロック数
    form = 0    #ミノの種類
    mode = 0    #ミノの向き
    y = -1     #ミノのy座標
    x = 4     #ミノのx座標
    speed = 500     #落下速度
}