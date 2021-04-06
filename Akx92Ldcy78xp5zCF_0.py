
def custom_sort(t, s):
    set_t = set(ord(c) for c in t)
    d = {c: i for i, c in
         enumerate(list(t) + [chr(i) for i in range(97, 123)
                              if i not in set_t])}
    return "".join(sorted(list(s), key=lambda c: d[c]))

