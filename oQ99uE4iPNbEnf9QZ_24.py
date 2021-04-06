
def no_perms_digits(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    
    return len(str(s))

