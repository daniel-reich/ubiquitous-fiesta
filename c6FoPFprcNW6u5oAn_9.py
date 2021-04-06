
def reduce(frac):
    nums = frac.split('/')
    numer = int(nums[0])
    denom = int((nums[1]))
​
    for i in range(2, denom + 1):
        while numer % i == 0 and denom % i == 0:
            numer, denom = int(numer / i), int(denom / i)
        
    return str(numer) + '/' + str(denom)
​
print(reduce('100/100'))
​
def farey(num):
    out = ['0/1']
    for i in range(num + 1):
        for a in range(1, i + 1):
            string = str(a) + '/' + str(i)
            if reduce(string) not in out:
                out.append(reduce(string))
    out = sorted(out, key = sortKey)
    return out
def sortKey(frac):
    nums = frac.split('/')
    numer = int(nums[0])
    denom = int((nums[1]))
    return numer / denom

