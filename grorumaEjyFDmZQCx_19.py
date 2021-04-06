
def is_wristband(lst):
    return all(len(set(i))==1 for i in lst) or \
        all(len(set(i))==1 for i in zip(*lst)) or \
        all(a[1:]==b[:-1] for a, b in zip(lst, lst[1:])) or \
        all(a[:-1]==b[1:] for a, b in zip(lst, lst[1:]))

