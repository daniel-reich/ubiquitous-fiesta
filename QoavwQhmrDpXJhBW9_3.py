
def flip_list(lst):
    if lst == []:return []
    if isinstance(lst[0], int): return [[i] for i in lst]
    if isinstance([lst[0]], list): return [j for i in lst for j in i]

