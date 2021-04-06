
def is_slidey(n):
    for i in range(1,len(str(n))):
        if int(str(n)[i]) - int(str(n)[i-1]) not in [-1,1]:
            return False
    return True

