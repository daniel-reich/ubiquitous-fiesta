
def all_about_strings(txt):
  l = len(txt)
  half = l // 2
  first = txt[0]
  last = txt[-1]
  mid = txt[half] if l % 2 == 1 else txt[half-1:half+1]
  index = txt.find(txt[1], 2)
  sec_occ = "@ index {}".format(index) if index > -1 else "not found"
  return [l, first, last, mid, sec_occ]

