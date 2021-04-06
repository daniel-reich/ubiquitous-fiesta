
def sort_authors(lst):
    import operator
    ans = {idx: (i.strip('.').split(' ')[-1][0].lower()) for idx, i in enumerate(lst)}
    ans = sorted(ans.items (), key=operator.itemgetter (1))
    return [lst[(i[0])] for i in ans]

