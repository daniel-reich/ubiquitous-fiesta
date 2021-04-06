
reverse_odd = lambda txt: ' '.join([w[::-1 if len(w)%2 else 1] for w in txt.split()])

