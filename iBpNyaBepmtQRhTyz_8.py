
def c_cipher(msg, keyword):
    newKeyword = keyword
    newKeyword = sorted(newKeyword)
    colOrder = []
    for item in newKeyword:
        colOrder.append(keyword.index(item))
​
    if ' ' in msg:
        a = ''
        for i in range(len(msg)):
            if msg[i].isalpha() or msg[i].isnumeric():
                a += msg[i].lower()
        l = len(keyword)
        while len(a) % l != 0:
            a += 'x'
        temp = []
        for i in range((len(a)//l)):
            temp.append(a[:l])
            a = a[l:]
​
        myans = ''
        for item in colOrder:
            for r in range(len(temp)):
                myans += temp[r][item]
        return myans
    else:
        l = len(msg)
        c = len(keyword)
        r = l//c
        temp = []
​
        for i in range(r):
            t = []
            for j in range(c):
                t.append([])
            temp.append(t)
        z = 0
        for item in colOrder:
            for j in range(r):
                temp[j][item] = msg[z]
                z += 1
        myans = ''
        for i in range(len(temp)):
            myans += ''.join(temp[i])
​
        return myans

