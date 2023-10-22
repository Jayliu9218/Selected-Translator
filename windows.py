import time

import pyperclip

import main
import disp

while True:
    clip_last = pyperclip.paste()
    time.sleep(1)
    if pyperclip.paste() != clip_last:
        clip_this = pyperclip.paste()
        result = main.trans_main(clip_this)
        disp.trans_disp(result)