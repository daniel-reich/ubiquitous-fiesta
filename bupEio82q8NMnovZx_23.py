
def track_robot(instructions):
    posx=0
    posy=0
    d=[[]]
    for i in instructions:
        p=i.split(" ")
        d.append(p)
    d.pop(0)
    for s in d:
        
        if s[0]=="right":
            posx=posx+int(s[-1])
        elif s[0]=="left":
            posx=posx-int(s[-1])
        elif s[0]=="up":
            posy=posy+int(s[-1])
        else:
            posy=posy-int(s[-1])
    return [posx,posy]

