
def iso_group(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) >= 2:
        if type(iso_group(lst[:-1])) == int:
            if lst[-1] == iso_group(lst[:-1]):
                return [lst[-1], iso_group(lst[:-1])]
            elif lst[-1] > iso_group(lst[:-1]):
                return lst[-1]
            else:
                return iso_group(lst[:-1])
        elif type(iso_group(lst[:-1])) == list:
            if lst[-1] in iso_group(lst[:-1]):
                return iso_group(lst[:-1]).append(lst[-1])
            elif lst[-1] > iso_group(lst[:-1])[0]:
                return lst[-1]
            else:
                return iso_group(lst[:-1])

