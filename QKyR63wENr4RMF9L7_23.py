
def tweak_letters(txt, lst):
    alpha = "abcdefghijklmnopqrstuvwxyz"*3
​
    arr = []
    for i in range(len(txt)):
        arr.append(alpha[alpha.index(txt[i]) + lst[i]])
    return "".join(arr)

