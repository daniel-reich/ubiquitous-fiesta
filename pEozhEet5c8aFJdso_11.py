
def all_about_strings(txt):
  length = len(txt)
  first = txt[0]
  last = txt[-1]
  mid = ""
  sec_occ = "not found"
  if length % 2 == 0:
    mid += (txt[(length // 2) - 1] + txt[length // 2])
  else:
    mid += txt[length // 2]
  for i in range(2, length):
    if txt[i] == txt[1]:
      sec_occ = "@ index " + str(i)
  return [length, first, last, mid, sec_occ]

