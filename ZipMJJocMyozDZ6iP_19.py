
def group(lst, num):
    num_groups = len(lst)//num
    if len(lst)%num != 0:
        num_groups += 1
    groups = [[] for _ in range(num_groups)]
    for idx, element in enumerate(lst):
        groups[idx%num_groups].append(element)
    return groups

