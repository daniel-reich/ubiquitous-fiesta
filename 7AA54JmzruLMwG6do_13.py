
def is_icecream_sandwich(txt):
    if len(txt)<3 or len(set(txt)) == 1 or len(set(txt))>2:
        return False
    else:
        if len(txt)%2==0 and txt[:len(txt)//2]==txt[len(txt)//2:][::-1]:
            return True
        elif txt[:(len(txt)//2+1)]==txt[-(1+len(txt)//2):][::-1]:
            return True
        else:
            return False

