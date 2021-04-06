
def missing_letter(lst):
  seq = set(map(chr, range(ord(min(lst)), ord(max(lst)) + 1)))
  return seq.difference(set(lst)).pop()

