
char_at_pos = lambda r, s: r[len(r) & 1 ^ (s=='odd')::2]

