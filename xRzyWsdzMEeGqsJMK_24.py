
def maskify(txt):
    txt2=[]
    if len(txt) < 5:
        return txt
    else:
        for i in range(0,(len(str(txt)))-4):
            txt2.append('#')
        return "".join(txt2)+txt[(len(str(txt)))-4:]

