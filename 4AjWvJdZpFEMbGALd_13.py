
def who_goes_free(n, k):
    prisoners = list(range(n))
    k -= 1
    kill = k
    while len(prisoners) > 1:
        prisoners.pop(kill) 
        kill = (kill + k) % len(prisoners)
    return prisoners[0]

