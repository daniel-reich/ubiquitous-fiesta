
def sort_contacts(l, o):
    lst = sorted([a for a in l], key=lambda x: x.split()[1][0]) if l else []
    return lst if o == 'ASC' else lst[::-1]

