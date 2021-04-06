
def incremental_depth(lst):
    if len(lst) == 2:
        return [lst[0], [lst[1]]]
    ans = [lst[-1]]
    for el in lst[:-1][::-1]:
        ans = [el, ans]
    return ans

