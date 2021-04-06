
def is_prob_matrix(arr):
    for i in arr:
        if sum(i)!= 1:
            return False
        for j in i:
            if not(0<=j<=1):
                return False
    if len(arr) != list(map(lambda x: len(x),arr))[0]:
        return False
    return True

