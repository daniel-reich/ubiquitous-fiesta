
def landscape_type(lst):
    n = 1
    if max(lst) != lst[0] and max(lst) != lst[-1]:
        for x in range(len(lst))[0:-1]:
            if lst[x + 1] >= lst[x] and n == 1:
                n = 1
            elif lst[x+1] <= lst[x] and n == 1:
                n = 0
            elif lst[x+1] <= lst[x] and n == 0:
                n = 0
            elif lst[x+1] >= lst[x] and n == 0:
                return "neither"
        return "mountain"
    elif min(lst) != lst[0] and min(lst) != lst[-1]:
        for x in range(len(lst))[0:-1]:
            if lst[x + 1] <= lst[x] and n == 1:
                n = 1
            elif lst[x+1] >= lst[x] and n == 1:
                n = 0
            elif lst[x+1] >= lst[x] and n == 0:
                n = 0
            elif lst[x+1] <= lst[x] and n == 0:
                return "neither"
        return "valley"
    else:
        return "neither"

