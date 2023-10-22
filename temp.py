import tkinter
import time
import pyautogui

last_time = int(time.time())

# screenWidth, screenHeight = pyautogui.size()
x,y = pyautogui.position()
w,h = 200, 100

window = tkinter.Tk()
window.geometry("%dx%d+%d+%d" % (w,h, x, y)) # 距离屏幕左上角(400, 200)
window.wm_attributes('-topmost', 1)

window_label = tkinter.Label(window,text='yes')
window_label.pack()

temp_mark = 2
while temp_mark:

    time.sleep(2)
    if temp_mark:
        print(temp_mark)
        temp_mark -= 1
        window.mainloop()



print(1)
print(int(time.time()))

# 1697979972.4378932
# 1697979982.7980201

result = {
    "from": "en",
    "to": "zh",
    "trans_result": [
        {
            "src": "timid",
            "dst": "胆小的"
        }
    ]
}

result = {
    "from": "en",
    "to": "zh",
    "trans_result": [
        {
            "src": "Welcome to the Rust Book experiment, and thank you for your participation! First, we want to introduce you to the new mechanics of this experiment.",
            "dst": "欢迎来到Rust Book实验，并感谢您的参与！首先，我们想向你介绍这个实验的新机制。"
        }
    ]
}

result = {
    "from": "en",
    "to": "zh",
    "trans_result": [
        {
            "src": "Welcome to the Rust Book experiment, and thank you for your participation!",
            "dst": "欢迎来到Rust Book实验，并感谢您的参与！"
        },
        {
            "src": "First, we want to introduce you to the new mechanics of this experiment.",
            "dst": "首先，我们想向你介绍这个实验的新机制。"
        }
    ]
}