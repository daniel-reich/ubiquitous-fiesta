
def odds_vs_evens(num):
    
    str_num = str(num)
    odd  = sum([int(x) for x in str_num if int(x)%2!=0])
    even = sum([int(x) for x in str_num if int(x)%2==0])
    
    if odd > even:
        return 'odd'
    elif odd < even:
        return 'even'
    else:
        return 'equal'

