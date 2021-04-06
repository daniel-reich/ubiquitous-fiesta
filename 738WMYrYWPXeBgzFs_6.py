
def is_valid(txt):
  chars = set(txt)
  counts = [txt.count(c) for c in chars]
  return 'YES' if sum(counts) <= min(counts)*len(chars) + 1 else 'NO'

