
def compare_data(*args):
  t = [type(x) for x in args]
  return t.count(t[0])==len(t) if t else True

