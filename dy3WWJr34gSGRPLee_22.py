
def make_box(s):
  n = [("#"*s) for i in range(s)]
  n = [k if i == 0 or i == s-1 else "{}".format("#"+" "*(s-2)+"#") for i,k in enumerate(n)]
  return n

