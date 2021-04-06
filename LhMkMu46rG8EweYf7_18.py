
def sort_by_letter(lst):
  def key(w):
    for c in w:
      if c.isalpha():
        return ord(c)
  return sorted(lst, key = key)

