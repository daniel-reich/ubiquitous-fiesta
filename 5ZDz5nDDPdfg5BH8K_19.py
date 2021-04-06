
def only_5_and_3(n):
    flag = 0
    for i in range(1, n):
        for j in range(n):
            if ((3**i) + (5*j)) == n or 5*j == n:
                return True
                break
    else:
        return False

