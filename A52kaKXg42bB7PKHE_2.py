
def num_then_char(lst):
    nums, letters = [], []
    for L in lst:
        for a in L:
            if type(a) == str:
                letters.append(a)
            else:
                nums.append(a)
    nums.sort()
    letters.sort()
    L = nums + letters
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = L.pop(0)
    return lst

