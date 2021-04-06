
left_side = lambda l: [ sum(1 for e in l[:i] if e < l[i]) for i in range(len(l)) ]
right_side = lambda l: [ sum(1 for e in l[i:] if e < l[i]) for i in range(len(l)) ]

