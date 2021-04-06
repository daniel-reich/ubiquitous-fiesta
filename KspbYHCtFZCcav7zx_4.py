
def bill_split(spicy, cost):
    me = sum(c for s,c in zip(spicy,cost) if s=="S")
    friend = (sum(cost)-me)//2
    return [me+friend, friend]

