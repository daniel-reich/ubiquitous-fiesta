
cipher = {"a" : "k", "b" : "g", "c" : "m", "d" : "q", "e" : "u", "f" : "t",
        "g" : "b", "h" : "x", "i" : "z", "j" : "o", "k" : "a", "l" : "n",
        "m" : "c", "n" : "l", "o" : "j", "p" : "w", "q" : "d", "r" : "y",
        "s": "v", "t": "f", "u": "e", "v": "s", "w": "p", "x": "h",
        "y": "r", "z": "i"}
​
def mubashir_cipher(message):
    message = message.lower()
    new_message = ""
    for letter in message:
        if letter in cipher:
            new_message += cipher[letter]
        else:
            new_message += letter
    return new_message

