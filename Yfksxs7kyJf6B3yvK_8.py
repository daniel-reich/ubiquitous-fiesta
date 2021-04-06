
def min_miss_pos(lst):
    restricted_zone=lambda x: list(i for i in set(x) if i >=0 )
    new_list=restricted_zone(lst)
    if len(new_list)==1:
        return new_list[0]+1
    for i in range(len(new_list)-1):
        if new_list[i]+1==new_list[i+1]:
            continue
        else:
            return new_list[i]+1
    else:
        return new_list[-1]+1
print(min_miss_pos([7, 6, 5, 4, 3, 2, 1]))

