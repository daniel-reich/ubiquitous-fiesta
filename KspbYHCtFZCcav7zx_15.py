
def bill_split(spicy, cost):
    a = sum( y if x =='S' else y/2 for x,y in zip(spicy, cost))
    b = sum( y/2 for x,y in zip(spicy, cost) if x =='N' )
    return [int(a), int(b)]

