
def major_sum(lst):
    pos = sum([i for i in lst if i > 0])
    neg = sum([i for i in lst if i < 0])
    zero = lst.count(0)
​
    if abs(neg) > pos and abs(neg) > zero :
        return neg
    else:
        return max(pos, zero)

