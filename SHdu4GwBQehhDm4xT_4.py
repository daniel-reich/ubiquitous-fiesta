
def freed_prisoners(prison):
    if prison[0] == 0: return 0
    lst = prison[:]
    count = 0
    for i in range(len(prison)):
        try:
            a = lst.index(1)
            count += 1
            lst = [1 if i == 0 else 0 for i in lst[a+1:]]
            print(lst)
        except:
            return count
    return count

