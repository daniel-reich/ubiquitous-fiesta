
def decrypt(s):
    a = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
​
    myans = ''
    i = len(s)-1
    while i >=0:
        if s[i] != '#':
            myans = a[int(s[i])] + myans
            i -= 1
        else:
            myans = a[int(s[i-2:i])] + myans
            i -= 3
    return myans

