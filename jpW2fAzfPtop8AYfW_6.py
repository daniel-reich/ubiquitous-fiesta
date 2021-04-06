
def to_dict(lst):
  return [dict([i]) for i in zip(lst,[ord(i) for i in lst])]

