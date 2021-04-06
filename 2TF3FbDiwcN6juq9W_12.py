
from datetime import date
​
def days_until_2021(d):
    M, D, Y = d.split('/')
    days = str((date(2021, 1, 1) - date(int(Y), int(M), int(D))).days)
    return days + ' days' if days != '1' else days + ' day'

