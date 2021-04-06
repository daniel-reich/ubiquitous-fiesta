
special_reverse=lambda s,c:" ".join([w[::1-2*(w[0]==c)]for w in s.split()])

