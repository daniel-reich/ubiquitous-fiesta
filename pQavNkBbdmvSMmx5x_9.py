
def majority_vote(lst):
    my_dict = {}
    for x in lst:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    
    for key in my_dict:
        if my_dict[key] > len(lst)//2:
            return key
    return None

