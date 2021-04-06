
from datetime import date as d
​
def days_until_2021(date):
    date = list(map(lambda x:int(x),date.split('/')))[::-1]
    ans =  ((d(2021,1,1)-d(date[0],date[2],date[1])).days)
    return str(ans)+' days' if ans!=1 else str(ans) + ' day'

