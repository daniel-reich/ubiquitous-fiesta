
def tallest_building_height(lst):
    for i in range(0,len(lst)):
        if lst[i].strip().startswith("#"):
            break
    return str((len(lst) - i) * 20 ) + "m"

