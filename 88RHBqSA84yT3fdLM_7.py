
def inator_inator(inv):
  return inv + 'inator {}'.format(str(len(inv * 1000))) if inv[-1].lower() not in ['a','e','i','o','u'] else inv + '-inator {}'.format(str(len(inv * 1000)))

