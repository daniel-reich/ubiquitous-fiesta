
def number_pairs(s):
    lst = s.split(' ')
    del lst[0]
    count = []
    for i in set(lst):
        count.append(lst.count(i)//2)
    return sum(count)

