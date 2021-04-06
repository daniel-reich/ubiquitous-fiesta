
def plus_sign(txt):
    text = [c for c in txt if c.isalpha()]
    r = [txt[char] for char in range(0,len(list(txt))-1) if txt[char].isalpha() and txt[char-1]=='+' and txt[char+1]=='+' and not txt[0].isalpha()]
    if len(r)==len(text):
        return True
    else:
        return False

