
def keyboard_mistakes(txt):
    lst=''
    for i in txt:
        if i =='4':
            lst += 'A'
        elif i == '5':
            lst += 'S'
        elif i == '0':
            lst += 'O'
        elif i == '1':
            lst +='I'
        else:
            lst += i
    return lst

