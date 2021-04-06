
def party_people(lst):
    if lst and max(lst) > len(lst):
        lst.pop(lst.index(max(lst)))
        return party_people(lst)
    else:
        return len(lst)

