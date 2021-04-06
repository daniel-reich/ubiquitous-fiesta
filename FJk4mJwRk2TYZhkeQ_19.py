
accum = lambda w: '-'.join(str.capitalize(w[i-1]*i) for i in range(1, len(w)+1))

