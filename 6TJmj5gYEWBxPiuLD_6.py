
def seating_students(lst):
    k, res = lst.pop(0), []
    arr = {i for i in range(1, k+1) if i not in lst}
    
    for i in arr:
        options = [(i, i-2), (i, i+1 if i%2 else i-1), (i, i+2)]
        for a, b in options:
            if 1 <= a <= k and b in arr and sorted([a, b]) not in res:
                res += [[a, b]]
    return len(res)

