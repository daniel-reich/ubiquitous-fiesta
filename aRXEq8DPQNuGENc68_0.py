
def salt(t):
    salt=10
    while t>=0:
        t-=1/6000   #millisecond increments 
        salt+=(.1-10*salt/100)/6000
    return round(salt,3)

