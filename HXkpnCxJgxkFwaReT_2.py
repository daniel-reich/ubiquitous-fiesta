
def count_datatypes(*args):
  t = {int:0, str:1, bool:2, list:3, tuple:4, dict:5}
  res = [0,0,0,0,0,0]
  for arg in args:
    res[t[type(arg)]] += 1
  return res

