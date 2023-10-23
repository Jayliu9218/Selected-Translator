import time
import pyperclip
import trans_main
import trans_disp


def run():
    while True:
        clip_last = pyperclip.paste()
        time.sleep(1)

        if pyperclip.paste() != clip_last:
            clip_this = pyperclip.paste()
            result = trans_main.trans_main(clip_this)
            trans_disp.trans_disp(result)


run()
