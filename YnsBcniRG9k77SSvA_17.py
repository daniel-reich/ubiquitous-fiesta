
def print_all_groups():
    letters = ["a", "b", "c", "d", "e"]
    groupsYears = []
    for y in range(1, 7):
        for g in letters:
            groupsYears.append(str(y) + g)
    return ", ".join(groupsYears)

