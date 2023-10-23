import tkinter
import pyautogui


def trans_disp(result):
    trans_result = result["trans_result"]
    print("src :", str(trans_result[0]["src"]))
    for trans in trans_result:
        print("dst :", str(trans["dst"]))

    x, y = pyautogui.position()
    w, h = 200, 100

    window = tkinter.Tk()
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.wm_attributes('-topmost', 1)

    for trans in trans_result:
        print("dst :", str(trans["dst"]))
        tkinter.Label(window, text=trans["dst"]+"\n").pack()

    window.mainloop()
