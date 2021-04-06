
def is_harshad(num):
    s=sum([int(i) for i in str(num)])
    if s==0 or num%s!=0:
        return False
    else:
        return True

