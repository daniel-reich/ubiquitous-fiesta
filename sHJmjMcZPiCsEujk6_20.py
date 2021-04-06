
PI = [int(_) for _ in "314159265358979"]
​
def pilish_string(txt):
    ans = []
    idx = 0
    while len(txt) > 0 and idx < len(PI):
        l = PI[idx]
        word = txt[:l]
        while len(word) < l:
            word += word[-1]
        ans.append(word)
        txt = txt[l:]
        idx += 1
    return ' '.join(ans)

