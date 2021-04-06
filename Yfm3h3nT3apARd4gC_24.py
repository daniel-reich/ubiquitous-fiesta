
def rolls(lst):
    for i in range(len(lst)-1, 0, -1):
        if lst[i-1] == 1:
            lst[i] = 0
        elif lst[i-1] == 6:
            lst[i] = 2*lst[i]
    return sum(lst)

