
def group(lst, size):
    start_list = sorted(lst, reverse=True)
    length = len(start_list)
    groups = int(len(lst) / size)
    if len(lst) / size > int(groups):
        groups = groups + 1
    master_list = [[] for i in range(groups)]
    while len(start_list) > 0:
        for i in range(0,len(master_list)):
            if len(start_list) > 0:
                a = start_list.pop()
                print(a)
                master_list[i].append(a)
            else:
                pass
    return master_list

