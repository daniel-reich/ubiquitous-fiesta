
def is_prob_matrix(lst):
    for i in lst:
        sum = 0
        if len(i) != len(lst):
            return False
        for j in i:
            if j < 0 or j > 1:
                return False
            sum += j
        if sum != 1:
            return False
    return True

