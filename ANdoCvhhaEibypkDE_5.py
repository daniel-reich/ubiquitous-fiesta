
def closing_in_sum(n, s=None, t=None):
  return closing_in_sum(n, str(n), 0) if t is None \
    else t + int(s) if len(s) == 1 else t if len(s) == 0 \
    else closing_in_sum(n, s[1:-1], t + int(s[0] + s[-1]))

