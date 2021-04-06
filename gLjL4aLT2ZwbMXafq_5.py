
def fair_swap(l1, l2):
  if (sum(l1) + sum(l2)) % 2 == 1:
    return set()
  avg = (sum(l1) + sum(l2))//2
  pair2 = lambda x: avg - (sum(l1)-x)
  pairs = [(el,pair2(el)) for el in list(set(l1)) if pair2(el) in l2]
  sorted_pairs = sorted(pairs)
  return set(sorted_pairs)

