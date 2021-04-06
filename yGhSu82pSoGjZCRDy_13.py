
def seesaw(num):
    if num == None or len(str(num))==1:
        return "balanced"
    else:
        num=str(num)
        if len(num)%2==0:
            a, b = str(num)[:len(num)//2], str(num)[len(num)//2:]
        else:
            a, b = str(num)[:len(num)//2], str(num)[len(num)//2+1:]
        return "left" if int(a)>int(b) else "right" if int(a)<int(b) else "balanced"

