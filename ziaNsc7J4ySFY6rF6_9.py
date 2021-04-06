
def will_fit(holds, cargo):
    x=0
    for i in holds:
        if i=='M':
            x+=100
        elif i=='S':
            x+=50
        elif i=='L':
            x+=200
    if sum(cargo)<x:
        return True
    else:
        return False

