
import math
def get_number_of_apples(n, p):
    new_p=p.replace('%','')
    new_p=int(new_p)
    apples_eaten=math.ceil((new_p*n)/100)
    if n-apples_eaten>0:
        return n-apples_eaten
    else:
        return 'The children didn\'t get any apples'

