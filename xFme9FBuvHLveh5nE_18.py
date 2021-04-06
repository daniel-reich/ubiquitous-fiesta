
def is_zygodrome(num):
  snum = str(num)
  if len(snum) < 2:
    return False
  cnt = 1
  chk = snum[0]
  for c in snum[1:]:
    if c != chk:
      if cnt < 2:
        return False
      cnt = 0
      chk = c
    cnt += 1
  return cnt > 1

