import tkinter
import pyautogui

def trans_disp(result):
    trans_result = result["trans_result"]
    print("src :", str(trans_result[0]["src"]))
    size_lines = 0
    size_chars = 0
    for trans in trans_result:
        print("dst :", str(trans["dst"]))
        size_lines += 1
        size_chars += len(str(trans["dst"]))

    x, y = pyautogui.position()
    w, h = 400, (size_chars / 13 + size_lines) * 15

    window = tkinter.Tk()
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.wm_attributes('-topmost', 1)

    for trans in trans_result:
        print("dst :", str(trans["dst"]))
        tkinter.Label(window, text=trans["dst"], justify='left', wraplength=380, anchor='w').pack()

    window.mainloop()