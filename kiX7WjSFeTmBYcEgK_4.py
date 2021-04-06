
def major_sum(lst):
    pos = sum([a for a in lst if a > 0])
    zeros = lst.count(0)
    neg = sum([a for a in lst if a < 0])
    return max(pos, zeros, neg,key=lambda x: abs(x))

