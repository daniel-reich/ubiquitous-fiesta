
def sum_of_slices(lst):
    sum = 0
    sol = []
    for num in lst:
        if sum + num >= 100:
            sol.append(sum)
            sum = 0
        sum += num
    if sum > 0:
        sol.append(sum)
    return sol

