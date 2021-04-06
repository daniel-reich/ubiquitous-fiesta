
def upward_trend(lst):
    for index in range (len(lst) -1):
        if isinstance(lst[index], str) or isinstance(lst[index + 1], str): return "Strings not permitted!"
        if lst[index] > lst[index + 1] :
            return False
    return True

