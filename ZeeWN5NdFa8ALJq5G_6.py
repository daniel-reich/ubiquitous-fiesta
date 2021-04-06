
def nearest_chapter(chapt, page):
  p = []
  for i, j in chapt.items():
    p += [(i, abs(page-j), j)]
  s = sorted(p, key=lambda x:(x[1], -x[2]))
  return s[0][0]

