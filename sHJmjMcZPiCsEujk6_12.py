
import math
def pilish_string(txt):
    strPi = str(math.pi)
    strPi = strPi[0] + strPi[2:16]
    print(strPi)
​
    res = ''
    piPos = 0
    txtPos = 0
    c = ' '
​
    if(len(txt) == 0):
        return res
    for i in range(len(strPi)):
        ch = strPi[i]
        for cnt in range(int(ch)):
            if(txtPos < len(txt)):
                c = txt[txtPos]
                res = res + c
                txtPos += 1
            else:
                res = res + c
        if(txtPos >= len(txt)):
            return res
        if(i < len(strPi) - 1):
            res = res + ' '
    return res

