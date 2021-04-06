
import string 
​
def digital_decipher(eMessage, key):
    l = list(string.ascii_lowercase)
    n = [i for i in range(1, 27)]
    d = dict(zip(n, l))
    skey = str(key)
    r = ''
​
    counter = 0
    if len(skey) < len(eMessage):
        diff = len(eMessage) - len(skey)
        for i in range(diff):
            ak = list(map(int, skey + skey[counter]))
​
    for i in range(len(eMessage)):
        if counter < len(eMessage): 
            if counter == len(skey):
                counter = 0
            r = r + (d[eMessage[i] - ak[counter]])
        counter += 1
    return r

