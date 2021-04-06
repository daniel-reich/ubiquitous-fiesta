
def check(lst):
    mini = min(range(len(lst)), key=lst.__getitem__)
    if sorted(lst) == lst: return "NO"
    return 'YES' if lst[mini:] +  lst[:mini] == sorted(lst) else 'NO'

