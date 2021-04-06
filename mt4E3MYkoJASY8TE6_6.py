
from itertools import product
​
def crack_pincode(pin):
    d = {'1': '124', '2': '2135', '3': '326', '4': '4157', '5': '52468', 
         '6': '6359', '7': '748', '8': '85790', '9': '968', '0': '08'}
    
    arr = [list(d[n]) for n in pin]
    return sorted([''.join(i) for i in product(*arr)])

