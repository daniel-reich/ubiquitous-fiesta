
def number_groups(group1, group2, group3):
    data = []
    for i in group1:
        if i in group2 and i not in data:
            data.append(i)
        if i in group3 and i not in data:
            data.append(i)
    for i in group2:
        if i in group3 and i not in data:
            data.append(i)
    data.sort()
    return data

