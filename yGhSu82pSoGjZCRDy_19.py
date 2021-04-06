
def seesaw(num):
    x = str(num)
    a,b = (x[:len(x)//2],x[len(x)//2:]) if len(x)%2==0 else (x[:len(x)//2],x[(len(x)//2)+1:])
    if a==b or x=='None':
        return "balanced"
    else:
        return "right" if b>a else "left"

