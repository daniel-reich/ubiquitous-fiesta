
def same_upsidedown(ntxt):
  m = len(str(ntxt)) // 2
  for i in range(m + 1):
    l = len(ntxt) - i - 1
    if str(ntxt)[i] == str(ntxt)[l] and (str(ntxt)[i] != "0" and str(ntxt)[l] != "0"):
      return False
  return True

