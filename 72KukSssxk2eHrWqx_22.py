
char_at_pos = lambda r,s: r[len(r)%2 if s=="even" else 1-len(r)%2::2]

