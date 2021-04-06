
def can_see_stage(list1):
    return not bool([list1[y][z] for z in range(0, len(list1[0])) for y in range(len(list1)-1, -1, -1) if (y != len(list1)-1 and list1[y][z] >= list1[y+1][z])])

