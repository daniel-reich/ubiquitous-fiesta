
def who_goes_free(n, k):
    prisoners = list(range(n))
    i = k-1
    while len(prisoners) > 1:
        if i < len(prisoners):
            prisoners[i] = -1
            i += k
        else:
            i = i - len(prisoners)
            prisoners = [prisoner for prisoner in prisoners if prisoner != -1]
    return prisoners[0]

