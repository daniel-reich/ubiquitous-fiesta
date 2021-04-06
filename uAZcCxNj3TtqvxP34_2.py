
mode=lambda l:sorted({n for n in l if l.count(n)==max(map(l.count,l))})

