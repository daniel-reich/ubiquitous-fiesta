
def shared_digits(lst):
    for i in range(1,len(lst)):
        if len(set(list(map(lambda x:int(x),list(str(lst[i]))))).intersection(set(list(map(lambda x:int(x),list(str(lst[i-1])))))))<1:
            return False
    return True

