
def camelCasing(txt):
  ans = "".join(l for l in txt.title() if l.isalpha())
  return ans[0].lower() + ans[1:]

