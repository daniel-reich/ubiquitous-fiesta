
def advanced_sort(lst):
    adv_lst = []
    for i in lst:
        group = [j for j in lst if j == i]
        if group not in adv_lst:
            adv_lst.append(group)
    return adv_lst

