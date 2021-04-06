
def to_dict(lst):
  return [] if not lst else [{x: ord(x)} for x in lst]

