
def comments_correct(txt):
  for a,b in [["/*","a"],["*/","b"],["//",""]]: txt = txt.replace(a,b)
  return not txt.replace("ab","")

