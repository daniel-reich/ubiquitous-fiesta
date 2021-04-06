
CTRLV = "Ctrl + V"
CTRLC = "Ctrl + C"
​
def keyboard_shortcut(txt):
    words = txt.split()
    l = len(words)
    ans = []
    buffer = []
    idx = 0
    while idx < l:
        word = words[idx]
        if word == "Ctrl":
            if idx < l - 2 and words[idx + 1] == "+" and words[idx + 2] == "C":
                # Ctrl + C:
                buffer = ans[:]
                idx += 2
            elif idx < l - 2 and words[idx + 1] == "+" and words[idx + 2] == "V":
                # Ctrl + V:
                ans += buffer
                buffer = []
                idx += 2
            else:
                ans.append(word)
        else:
            ans.append(word)
        idx += 1
    return ' '.join(ans)

