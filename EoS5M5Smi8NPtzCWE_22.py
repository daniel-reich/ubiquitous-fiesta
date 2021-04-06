
def secret(text):
    t = text.split('*')
    t[1] = int(t[1])
​
    myans = ''
​
    temp = '<'+t[0]+'></'+t[0]+'>'
​
    myans = t[1]*temp
​
    return myans

