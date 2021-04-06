
def tallest_building_height(lst):
    count = 0
    for x in lst:
        if x.strip(' ')[0:1] == '#':
            count += 1
    return str(count*20)+'m'

