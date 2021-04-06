
printgrid = lambda r, c: [list(i) for i in zip(*[range(1, r*c+1)[i:i+r] for i in range(0, r*c, r)])]

