
def number_pairs(txt):
  chk = set()
  cnt = 0
  for n in list(map(int,txt.split()))[1:]:
    if n in chk:
      cnt += 1
      chk.remove(n)
    else:
      chk.add(n)
  return cnt

