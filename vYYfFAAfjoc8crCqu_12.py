
def tree(h):
  return [('{ch:^{width}}').format(ch='#'*(2*i + 1), width=2*h - 1) for i in range(h)]

