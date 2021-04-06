
colors = {"R", "G", "B"}
def coloured_triangle(row):
    lst = list(row)
    while len(lst) > 1:
        for i in range(len(lst) - 1):
            if lst[i] != lst[i + 1]:
                lst[i] = (colors - {lst[i], lst[i + 1]}).pop()
        lst = lst[: -1]
    return lst[0]

