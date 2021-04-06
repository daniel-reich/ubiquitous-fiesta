
def journey_distance(n):
    km=0
    if n>=3:
        n-=3
        km+=1
    while n!=0:
        n-=2
        km+=1
    return km

