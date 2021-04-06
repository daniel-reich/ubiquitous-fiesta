
def new_ways(a,b):
    l = len(b)
    temp = [0 for x in range(a)]
    temp[0] = 1
    temp[1] = 1
​
    for i in range(2,a):
        j = 1
        while j <= l and j <= i:
            temp[i] += temp[i-j]
            j += 1
    return temp[a-1]
​
def num_ways(n, s):
    return new_ways(n+1,s)

