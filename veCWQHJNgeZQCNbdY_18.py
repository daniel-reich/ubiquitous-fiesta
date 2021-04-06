
def root_digit(n):
    if len(str(n))==1:
        return n
    else:
        l=(n%10)+root_digit(n//10)
        if len(str(l))==1:
            return l
        else:
            return (l%10)+root_digit(l//10)

