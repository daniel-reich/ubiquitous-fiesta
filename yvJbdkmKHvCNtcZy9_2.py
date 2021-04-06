
def is_disarium(n):
    count = 1
    orginal = n
    
    n = str(n)
    result = 0
    disarium = None
    for val in n:
        val = int(val)
        result += val**count
        count += 1
​
    
    if(orginal == result):disarium =True
    else: disarium = False
​
    return(disarium)

