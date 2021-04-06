
def order(lst):
  return [i for i,v in sorted(enumerate(lst), key=lambda kv: kv[1])]

