
def tallest_building_height(lst):
    ht = 0
    for line in lst:
        if "#" in line:
            ht += 1
    return str(ht*20)+"m"

