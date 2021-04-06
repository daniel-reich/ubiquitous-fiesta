
def over_time(lst):
    if lst [0] > 17 and lst[1] > 17:
        return "${:.2f}".format(((lst[1] - lst[0]) * lst[2] * lst[3]) + 0.001)
    elif lst[1] > 17:
        return "${:.2f}".format(((lst[1] - 17) * lst[2] * lst[3]) + (((lst[1] - lst[0]) - (lst[1] - 17)) * lst[2])+0.001)
    return "${:.2f}".format((lst[1] - lst[0]) * lst[2] + 0.001)

