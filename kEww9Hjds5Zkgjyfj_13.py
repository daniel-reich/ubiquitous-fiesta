
def replace_next_largest(l):
  return [ sorted(l)[sorted(l).index(e)+1] if e != max(l) else -1 for e in l ]

