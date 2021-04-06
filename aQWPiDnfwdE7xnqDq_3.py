
def drange(*args):
    lst = [i for i in args] 
    if len(lst) == 1:
        return tuple(range(lst[0]))
    ans = []
    digit = max(len(str(float(i))[str(float(i)).index('.'):]) for i in lst)
    if len(lst) == 2:
        for i in range(int(lst[0]),int(lst[1])):
            ans.append(i + lst[0] % 1)
    else:
        ans.append(lst[0])
        while lst[0] + lst[2] < lst[1]:
            lst[0] += lst[2]
            ans.append(round(lst[0],digit))
    return tuple(ans)

