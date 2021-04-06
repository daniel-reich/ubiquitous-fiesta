
def maskify(txt):
    if(len(txt)<=4):
        return txt
    else:
        y=txt[:-4]
        z=txt[-4:]
        for i in y:
            y=y.replace(i,"#")
​
​
        return y+z

