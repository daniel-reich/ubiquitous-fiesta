
def party_people(lst):
    if len(lst) == 0:
        return 0
    return len(lst) if max(lst) <= len(lst) else party_people([k for k in lst if k <= len(lst)])

