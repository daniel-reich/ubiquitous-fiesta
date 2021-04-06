
obj ={'1':'I','2':'Z','3':'E','4':'H','5':'S','6':'G','7':'L','8':'B','9':'-',
'0' :'O',}
​
def turn_calc(num):
    l = list(str(num))[::-1]
    s =''
    for char in l:
        if char in obj: s+=obj[char]
        else :s+=''
    return  s

