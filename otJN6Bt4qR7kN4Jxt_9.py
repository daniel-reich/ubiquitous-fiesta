
def incremental_depth(lst):
    res = [lst[0], [lst[1]]]
    for i, val in enumerate(lst[2:]):
        exec('res{}.append([val])'.format('[1]' * (i + 1)))
    return res

