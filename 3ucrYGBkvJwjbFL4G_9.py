
def reversible_inclusive_list(s, e, r=False):
  return reversible_inclusive_list(e, s, True) if s > e else [s] if s >= e \
    else sorted((reversible_inclusive_list(s, e - 1) + [e]), reverse=r)

