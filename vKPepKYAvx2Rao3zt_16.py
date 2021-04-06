
def car_timer(n):
    h = str(n // 60)
    m = str(n % 60)
    
    myans = 0
    for i in h:
        myans += int(i)
    for i in m:
        myans += int(i)
    return myans

