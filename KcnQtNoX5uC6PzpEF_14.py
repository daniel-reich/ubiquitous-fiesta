
def check_sum(lst, n):
  for eachnumber in lst:
    for eachnumber2 in lst:
      if eachnumber == eachnumber2:
        continue
      else:
        if eachnumber + eachnumber2 == n:
          return True
  return False

