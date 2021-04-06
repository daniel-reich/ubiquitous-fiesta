
def neighboring(txt,s=''):
    if txt[::-1]==txt and txt[0]!=txt[1]:return True
    for i in range(ord(txt[0]),ord(txt[-1])+1):
        s+=chr(i)
    return  True if txt==s else False

