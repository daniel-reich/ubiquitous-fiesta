
def clear_ordering(lst):
    a = [lst[i][0]for i in range(len(lst))]
    b = [lst[i][1]for i in range(len(lst))]
    return len(set(b))==len(b)and len(set(a))==len(a)

