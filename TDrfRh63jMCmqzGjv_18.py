
def is_anti_list(lst1, lst2):
    if lst1[0] != lst2[0] and lst1[1] != lst2[1]:
        pairs = {lst1[0]: lst2[0], lst1[1]: lst2[1]}
        for i in range(2, len(lst1)):
            if lst1[i] != pairs[lst2[i]]:
                return False
        return True
    return False

