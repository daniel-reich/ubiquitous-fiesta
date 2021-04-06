
def check_sum(lst, n):
    for i in lst:
        for j in lst:
            if i + j == n:
                return True
    return False

