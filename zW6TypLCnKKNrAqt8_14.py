
left_side=lambda l:[sum(a>b for b in l[:i])for i,a in enumerate(l)]
right_side=lambda l:left_side(l[::-1])[::-1]

