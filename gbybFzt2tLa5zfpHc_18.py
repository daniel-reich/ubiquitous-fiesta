
def three_sum(lst):
  sols = []
  for ka, va in enumerate(lst[:-2]):
    for kb, vb in enumerate(lst[ka+1:-1]):
      for kc, vc in enumerate(lst[ka+1+kb+1:]):
        if sum([va, vb, vc]) == 0:
          if [va, vb, vc] not in sols:
            sols.append([va, vb, vc])
  return sols

