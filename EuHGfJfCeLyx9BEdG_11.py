
def party_people(lst):
    if len(lst) < min(lst) and max(lst) > len(lst):
        return 0
    
    if max(lst) > len(lst):
        return party_people([i for i in lst if i != max(lst)])
    
    return len(lst)

