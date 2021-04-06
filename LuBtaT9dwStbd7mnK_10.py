
def tallest_building_height(lst):
    for h in range(len(lst)):
        if '#' in lst[h]:
            break
    return str((len(lst) - h) * 20) + 'm'

