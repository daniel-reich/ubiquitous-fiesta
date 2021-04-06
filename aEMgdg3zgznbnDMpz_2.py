
def check(w):
    for i in w:
        if i not in ["H", "I", "N", "O", "S", "X", "Z","W","M"]:return False
    return 1
​
def rotated_words(txt):
    return list(map(check,set(txt.split(" ")))).count(1) if  txt else 0

