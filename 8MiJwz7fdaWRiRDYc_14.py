
def apocalyptic(n):
    b=str(pow(2, n))
    mylst=[]
    for i in range(len(b)-2):
        if b[i]==b[i+1]==b[i+2]=="6":
            mylst.append(i)
    if len(mylst)!=0:
        return "Repent! {} days until the Apocalypse!".format(min(mylst))
    else:
        return  "Crisis averted. Resume sinning."

