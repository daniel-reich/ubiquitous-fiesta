
def sort_contacts(names, sort):
    if names == None: return []
    array = [[i.split()[1], i.split()[0]] for i in names]
    if sort == 'ASC':
        array = sorted(array)
    elif sort == 'DESC':
        array = sorted(array, reverse = True)
    return [firstname + ' ' + surname for surname, firstname in array]

