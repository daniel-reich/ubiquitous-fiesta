
def get_items_at(r, k):
  return [] if not len(r) else [[], [r[0]]][bool(len(r) % 2 and
  k == 'odd' or not(len(r) % 2) and k == 'even')] + get_items_at(r[1:], k)

