
code_list = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "j"],
    ["l", "m", "n", "o", "p"],
    ["q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z"],
]
​
code_dict = {
    "a": ". .",
    "c": ". ...",
    "b": ". ..",
    "e": ". .....",
    "d": ". ....",
    "g": ".. ..",
    "f": ".. .",
    "i": ".. ....",
    "h": ".. ...",
    "k": ". ...",
    "j": ".. .....",
    "m": "... ..",
    "l": "... .",
    "o": "... ....",
    "n": "... ...",
    "q": ".... .",
    "p": "... .....",
    "s": ".... ...",
    "r": ".... ..",
    "u": ".... .....",
    "t": ".... ....",
    "w": "..... ..",
    "v": "..... .",
    "y": "..... ....",
    "x": "..... ...",
    "z": "..... .....",
}
​
​
def tap_code(text):
    if "." in text:
        return code_to_text(text)
    return text_to_code(text)
​
​
def code_to_text(code):
    output_text = ""
    a = code.split(" ")
    b = zip(a[::2], a[1::2])
    for c in b:
        output_text += code_list[len(c[0]) - 1][len(c[1]) - 1]
    return output_text
​
​
def text_to_code(text):
    output_text = ""
    for c in text:
        output_text += code_dict[c] + " "
    return output_text.strip()

