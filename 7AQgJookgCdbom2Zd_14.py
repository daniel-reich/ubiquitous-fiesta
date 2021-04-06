
def pig_latin(txt):
    v = "aeiou"
    s = txt.lower().replace(".", "").replace("!", "").split()
    arr = []
    for i in range(len(s)):
        if s[i][0] not in v:
            arr.append(s[i][1:] + s[i][0] + "ay")
        else:
            arr.append(s[i] + "way")
​
    answer = " ".join(arr) + txt[-1]
​
    return answer[0].upper() + answer[1:]

