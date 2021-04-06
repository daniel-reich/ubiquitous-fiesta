
def alternate_sort(lst):
    l1 = [ x for x in lst if x == str(x)]
    l2 = [x for x in lst if x!=str(x)]
    l1.sort(),l2.sort()
    ls=[]
    for i,j in zip(l1,l2):
        ls.append(j),ls.append(i)
    return ls
print(alternate_sort(["a", "b", "c", 1, 2, 3]))

