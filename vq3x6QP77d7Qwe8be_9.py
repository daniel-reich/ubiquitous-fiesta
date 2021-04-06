
def odd_square_patch(lst):
    max_width = min(len(lst), len(lst[0]))
    rlst = list(map(lambda r: list(map(lambda e: e%2, r)), lst))
    for width in range(max_width+1,0,-1):
        for i in range(len(lst)-width+1):
            for j in range(len(lst[0])-width+1):
                if all(map(lambda x: x == 1, [rlst[p][q] for p in range(i,i+width) for q in range(j,j+width)])):
                    return width
    return 0

