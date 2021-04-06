
def lines_are_parallel(l1,l2):                       #                         0   1   2
    new_l1 = [l1[1]/l1[1],-l1[0]/l1[1],l1[2]/l1[1]]  # y = mx + b conversion, [y, mx , b]
    new_l2 = [l2[1]/l2[1],-l2[0]/l2[1],l2[2]/l2[1]]
    # print(new_l1)
    # print(new_l2)
    if new_l1[1] != new_l2[1]:
        return False
    if new_l1[1] == new_l2[1] and new_l1[2] == new_l2[2] or new_l1[2] != new_l2[2]:
        return True

