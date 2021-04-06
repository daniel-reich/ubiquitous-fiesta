
def check(lst):
    posi = sorted(lst)
    for i in range(0,len(lst)-1):
        first=posi.pop(0)
        posi.append(first)
        if posi==lst:
            return "YES"
​
    return 'NO'

