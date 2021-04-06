
import re
def group_seats(lst, n):
    rows = [''.join([str(i) for i in j]) for j in lst]
    seats = n*'0'
    extraseats = (n+1)*'0'
    return sum([1 for i in rows if re.search(seats, i)]) + sum([1 for i in rows if re.search(extraseats, i)])

