
def valid_color(s):
    sidx=edix=-1
​
    if s[0:4]=='rgb(':
        sidx=4
        name='rgb'
    elif s[0:5]=='rgba(':
        sidx=5
        name='rgba'
    else:
        return False
​
    if s[-1]==')':
        eidx=-1
    else:
        return False
​
    args=s[sidx:eidx].split(',')
​
    def isValidRGBV(vs):
        vs=vs.strip()
        return True if (vs.isdigit() and 0<=int(vs)<=255) or (vs[0:-1].isdigit() and vs[-1]=='%' and 0<=int(vs[0:-1])<=100) else False
​
    def isValidAlphaV(vs):
        vs=vs.strip()
        return True if (vs.replace('.','',1).isdigit() and 0<=float(vs)<=1.0) else False
​
    return True if (name=='rgb' and len(args)==3 and isValidRGBV(args[0]) and isValidRGBV(args[1]) and isValidRGBV(args[2])) or (name=='rgba' and len(args)==4 and isValidRGBV(args[0]) and isValidRGBV(args[1]) and isValidRGBV(args[2]) and isValidAlphaV(args[3])) else False

