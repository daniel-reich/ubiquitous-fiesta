
def is_prob_matrix(lst):
    if len(lst)==len(lst[0]):
        for i in lst:
            for j in i:
                if j>=0 and j<=1:
                    if sum(i)==1:
                        return True
                    else:
                        return False
                else:
                    return False
    else:
        return False

