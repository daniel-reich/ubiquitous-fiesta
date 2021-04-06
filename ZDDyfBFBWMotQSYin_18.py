
def is_harshad(num):
    if num==0:
        return False
    x=sum([int(i) for i in str(num)])
    return (num/x)==int(num/x)

