
def pages_in_book(num):
    x=0
    sum1 = 0
    while sum1!=num:
        sum1+=x
        x+=1
        if sum1>num:
            return False
            break
    return True

