
def camelCasing(txt):
    lst = txt.replace('_', ' ').lower().split()
    for i in range(1,len(lst)):
        lst[i] = lst[i].capitalize()
    return ''.join(lst)

