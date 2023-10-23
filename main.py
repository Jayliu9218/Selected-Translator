import time
import tkinter
import pyperclip
import pyautogui
import requests
import random
import json
from hashlib import md5


def trans_main(query):
    # Set your own appid/appkey.
    appid = '20231022001855764'
    appkey = 'PU6hcDIpCsKaTY86GABN'

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'en'
    to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'
    # query = 'timid'
    # query = 'Welcome to the Rust Book experiment, and thank you for your participation!\n First, we want to introduce you to the new mechanics of this experiment.'

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    return result


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


def run():
    while True:
        clip_last = pyperclip.paste()
        time.sleep(1)

        if pyperclip.paste() != clip_last:
            clip_this = pyperclip.paste()
            result = trans_main(clip_this)
            trans_disp(result)


run()
