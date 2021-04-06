
def replace_next_largest(lst):
    key = sorted(lst.copy())
    key2 = key.copy() + [-1]
    dic = {x : y for x, y in zip(key, key2[1:])}
    return [dic[x] for x in lst]

