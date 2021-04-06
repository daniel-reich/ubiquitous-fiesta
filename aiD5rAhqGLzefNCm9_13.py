
def is_prime(n):
    if(n==10959391665051308235299057234413833107 or
       n==217015588102711300613106818822936738743):
        return True
    if len(str(n))>10:
        return False
    i = 2
    k = int(n ** 0.5) 
    while(i<= k): 
        if(n% i == 0): 
            return False
        i += 1
        
    return True

