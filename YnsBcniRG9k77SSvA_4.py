
def print_all_groups():
    groups = ["a", "b", "c", "d", "e"]
    all_groups = ''
    for i in range(6):
        for g in groups:
            all_groups += (str(i+1) + g + ', ')
    return (all_groups[:-2])

