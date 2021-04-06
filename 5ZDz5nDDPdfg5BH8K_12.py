
def only_5_and_3(n):
    is_prim = True
    lst_numbers_lim = list(range(2, int(n/3)))
    for num_lim in lst_numbers_lim:
        if int(n/3) % num_lim == 0:
            is_prim = False
            break
        else:
            continue
​
    for i in range(100):
        for j in range(100):
            if (3**i + 5 * j == n and i != 0 and j != 0) or ((3 + (5*i))*3**j == n and i != 0 and j != 0) or not is_prim:
                return True
​
    if (n - (n//5)*5) == 3 or n % 15 == 0 or n % 5 == 0:
        return True
​
    return False

