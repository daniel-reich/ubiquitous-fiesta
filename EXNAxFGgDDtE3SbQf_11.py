
def shuffle_count(num,lst=[],orig=[], count=0):
    if orig == []:
        if num <= 1:
            return 0
        lst = []
        for i in range (1,num+1):
            lst.append(i)
        orig = lst.copy()
    half = len(lst)//2
    first = lst[:half]
    last = lst [half:]
    new = []
    for i in range(half):
        new.append(first[i])
        new.append(last[i])
    if new == orig:
        return count + 1
    return shuffle_count(num, new, orig, count+1)

