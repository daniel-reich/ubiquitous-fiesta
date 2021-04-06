
def palindrome_descendant(num):
  print(num)
  snum = str(num)
  if len(snum) == 1:
    return False
  if snum == snum[::-1]:
    return True
  if len(snum) == 2:
    return False
  vnum = [int(k) for k in snum]
  b = ''.join([str(vnum[k - 1] + vnum[k]) for k in range(1, len(vnum), 2)])
  return palindrome_descendant(int(b))

