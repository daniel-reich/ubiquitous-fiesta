
def nearest_chapter(c, p):
  r = [[k, abs(v-p)] for k, v in c.items()]
  m = min([v for k, v in r])
  return [k for k, v in sorted(r) if v == m][-1]

