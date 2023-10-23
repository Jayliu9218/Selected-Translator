

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
            "src": "timid",
            "dst": "胆小的"
        },
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

# trans_disp.trans_disp(result)
result = trans_main.trans_main("The syntax if let takes a pattern and an expression separated by an equal sign. It works the same way as a match, where the expression is given to the match and the pattern is its first arm. In this case, the pattern is Some(max), and the max binds to the value inside the Some. We can then use max in the body of the if let block in the same way we used max in the corresponding match arm. The code in the if let block isn’t run if the value doesn’t match the pattern.")

trans_disp.trans_disp(result)