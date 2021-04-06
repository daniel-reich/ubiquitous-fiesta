
def almost_palindrome(txt):
    fir = txt[:len(txt)//2]
    sec = txt[len(txt)//2:]
    fir = fir[::-1]
    if len(sec) > len(fir):
        sec = sec[1:]
    return sum(0 if fir[i] == sec[i] else 1 for i in range(len(fir))) == 1

