
def who_goes_free(n, k):
    t = range(0, n)
    t2 = h(t, k)
    return t2[0]
​
​
def h(lis, k):
    if len(lis) == 1:
        return lis
​
​
    if len(lis) < k:
        lis2 = lis.copy()
        lis3 = []
​
        if k % len(lis) == 0:
            del lis2[-1]
​
        else:
            lis3 = lis3 + lis2[k % len(lis):]
            del lis2[k%len(lis) -1:]
        lis3=lis3+lis2
        return h(lis3,k)
​
​
    lis2 = [lis[x] for x in range(len(lis)) if (x + 1) % k != 0]
    l = len(lis) - (len(lis) // k) * k
    lis3 = []
    lis3 = lis3 + lis2[len(lis2) - l:]
    del lis2[len(lis2) - l:]
    lis3 = lis3 + lis2
    return h(lis3, k)
print(who_goes_free(15, 4))

