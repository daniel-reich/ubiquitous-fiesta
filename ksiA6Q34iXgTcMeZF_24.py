
def bonus(days):
    if days<=32:
        return 0
    
    if days<=40:
        a=days-32
        return a*325
    
    if days<=48:
        a=days-40
        b=days-32-a
        return a*550+b*325
    
    if days>48:
        a=days-48
        b=days-40-a
        c=days-32-a-b
        return a*600+b*550+c*325

