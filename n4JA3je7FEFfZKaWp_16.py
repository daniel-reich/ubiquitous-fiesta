
def million_in_month(first_month, multiplier):
    n=0
    ans = first_month
    while ans<10**6:
        ans+= first_month*(multiplier**(n-1))
        n+=1
    return n-1

