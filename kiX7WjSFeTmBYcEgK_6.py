
def major_sum(lst):
    P = [i for i in lst if i >0]
    N = [u for u in lst if u <0]
    Z = lst.count(0)
    return max([sum(P),sum(N),Z],key=lambda x: abs(x))

