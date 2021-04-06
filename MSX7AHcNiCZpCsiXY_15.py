
import datetime
def how_unlucky(y):
    c = 0
    for i in range(1,13):
        if datetime.datetime(y,i,13).strftime('%a')=='Fri':c+=1
    return c

