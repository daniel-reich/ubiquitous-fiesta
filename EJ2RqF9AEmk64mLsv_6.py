
def lottery(ticket, win):
    s = lambda x,y:any(list(map(lambda i:ord(i)==y,list(x))))
    j=0
    for i in ticket:
        if s(i[0],i[1]):j+=1
    return "Winner!" if win<=j else "Loser!"

