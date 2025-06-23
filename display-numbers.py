# 在这里写上你的代码 :-)
from microbit import *

current_num = 1

while True:
    if button_a.was_pressed():  # 按下 A 按钮切换到下一个数字
        current_num += 1
        if current_num > 3:
            current_num = 1
        display.show(current_num)
    elif button_b.was_pressed():  # 按下 B 按钮清空屏幕
        display.clear()
