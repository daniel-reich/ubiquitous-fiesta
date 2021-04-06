
is_alpha = lambda w: not bool(sum(ord(k) for k in w if k.isalpha()) % 2)

