
def changeBase(num,b):
    ans = ''
    for i in range(20,-1,-1):
        z = num // b**i
        ans += str(num // b**i)
        num -= z * b**i
​
    return int(ans)
​
def esthetic(num):
    myans = []
    for i in range(2,11):
        t = str(changeBase(num,i))
        works = True
        for j in range(len(t)-1):
            if abs(int(t[j])-int(t[j+1])) != 1:
                works = False
                break
        if works:
            myans.append(i)
    if len(myans) > 0:
        return myans
    else:
        return 'Anti-Esthetic'

