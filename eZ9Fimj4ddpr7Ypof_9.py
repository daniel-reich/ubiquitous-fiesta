
def mumbling(s):
    myans = []
    for i in range(len(s)):
        temp = ''
        temp += s[i].upper()
        if i > 0:
            temp += s[i].lower() *(i)
        myans.append(temp)
​
    return '-'.join(myans)

