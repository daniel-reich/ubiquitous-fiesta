
def empty_values(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], int):
            lst[i] = 0
        elif isinstance(lst[i], float):
            lst[i] = float(0)
        elif isinstance(lst[i], str):
            lst[i] = ''
        elif isinstance(lst[i], bool):
            lst[i] = bool(1 - lst[i])
        elif isinstance(lst[i], list):
            lst[i] = []
        elif isinstance(lst[i], tuple):
            lst[i] = ()
        elif isinstance(lst[i], set):
            lst[i] = set()
        else:
            lst[i] = None
    return lst

