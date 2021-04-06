
def swap_prison(new_list):
    swap_list = []
    for elem in new_list:
        if elem == 0:
            swap_list.append(1)
        else:
            swap_list.append(0)
    return swap_list
​
​
def freed_prisoners(prison):
    i = 0
    count = 0
    while i < len(prison):
        if prison[i] == 1:
            count += 1
            prison = swap_prison(prison)
        elif prison[i] == 0 and i == 0:
            break
        i += 1
    return count

