
def is_parallelogram(lst):
    w = sorted(i[0] for i in lst)
    h = sorted(i[1] for i in lst)
    return w[0]-w[2] == w[1]-w[3] and h[0]-h[2] == h[1]-h[3]

