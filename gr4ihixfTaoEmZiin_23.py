
def add_indexes(lst):
    newlist = []
    for i in enumerate(lst):
        newlist.append(i[0] + i[1])
    return (newlist)

