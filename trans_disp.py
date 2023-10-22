import time
import tkinter
import pyautogui

def trans_disp(result):
    last_time = int(time.time())
    # print('from : ',str(result["from"]))
    # print('to : ',str(result["to"]))
    trans_result = result["trans_result"]
    print("src :",str(trans_result[0]["src"]))
    len_of_trans = 0
    for trans in trans_result:
        print("dst :",str(trans["dst"]))
        len_of_trans = len_of_trans + len(str(trans["dst"]))

    # screenWidth, screenHeight = pyautogui.size()
    x, y = pyautogui.position()
    w, h = 50*len_of_trans, 100

    window = tkinter.Tk()
    window_bool = 3
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))  # 距离屏幕左上角(400, 200)
    window.wm_attributes('-topmost', 1)

    window_label = tkinter.Label(window, text=trans_result)
    window_label.pack()

    if not window_bool:
        window.destroy()

    while window_bool:
        time.sleep(1)
        window_bool -= 1

        if window_bool:
            window.mainloop()


