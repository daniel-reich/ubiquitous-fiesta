
def who_goes_free(n, k):
    jump_adjust = k - 1
    prisoners = []
    for i in range (0,n):
            prisoners.append(i)
    index = 0
    while len(prisoners)> 1:
        index = index + jump_adjust
        while index >= len(prisoners):
            index = index - len(prisoners)
        prisoners.pop(index)
    return(prisoners[0])

