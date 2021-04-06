
def dice_game(scores):
    lop = ['p1', 'p2' , 'p3' , 'p4']
    beg = 0
    while len(lop) > 1:
        los = scores[beg:beg+len(lop)]
        beg = beg + len(lop)
        one_round(lop, los)
    return lop[0]
​
def one_round(lop, los):
    rnd = [(lop[i], sum(los[i]), los[i][0], los[i][1])
         for i in range(len(lop))]
    rank = sorted(rnd, key=lambda x: x[1:])
    if rank[0][1:] != rank[1][1:]:
        lop.remove(rank[0][0])
    return

