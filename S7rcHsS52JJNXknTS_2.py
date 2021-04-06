
def ink_levels(inks):
    lst = []
    for i in inks:
            lst.append(inks.get(i))
    return min(lst)

