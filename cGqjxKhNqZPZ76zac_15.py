
def fire(x, c):
    d = {"A":0,"B":1,"C":2,"D":3,"E":4}
    if x[d[c[0]]][int(c[1])-1]=='*':
        return "BOOM"
    else:
        return "splash"

