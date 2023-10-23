
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

print(result["trans_result"][1])