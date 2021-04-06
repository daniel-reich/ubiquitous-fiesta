
def paul_cipher(s):
    w = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    fl = ''
    for letter in s:
        if not fl and letter.isalpha():
            fl = True
            result+=letter
            n = w.index(letter.lower())+1
        elif letter.isalpha():
            r =  (n+ w.index(letter.lower())+1)
            result = result + w[(r-26)-1 if r >= 26 else r-1] 
            n = w.index(letter.lower())+1
        else:
            result+=letter
    return result.upper()

