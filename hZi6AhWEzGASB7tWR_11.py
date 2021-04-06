
def check(lst):
    new = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            new.append('in')
        else:
            new.append('de')
    if len(set(new)) == 2:
        return 'neither'
    elif set(new) == {'in'}:
        return 'increasing'
    else:
        return 'decreasing'

