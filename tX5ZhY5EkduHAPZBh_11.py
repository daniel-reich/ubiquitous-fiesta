
def nearest_element(n, lst):
    a = sorted([(abs(v-n), v, idx) for idx, v in enumerate(lst)])
    b = sorted([(v, idx) for d, v, idx in a if d == a[0][0]])
    return b[-1][1]

