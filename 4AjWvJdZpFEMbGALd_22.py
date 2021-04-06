
def who_goes_free(n, k):
    prisoners = list(range(n))
    left = 0
    while True:
        start = k-left-1
        left = (len(prisoners)-1-start)%k
        del prisoners[start::k]
        if len(prisoners) == 1:
            return prisoners[0]

