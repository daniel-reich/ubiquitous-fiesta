
def get_middle(s):
    if len(s) % 2 == 1:
        return s[int((len(s)-1)/2)]
    elif len(s) == 0:
        return ''
    else:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]

