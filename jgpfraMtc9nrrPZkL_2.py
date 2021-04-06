
def switch_gravity_on(lst):
    return list(map(list, zip(*map(sorted, zip(*lst)))))[::-1]

