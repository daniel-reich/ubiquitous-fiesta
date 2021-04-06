
def duplicates(txt):
  dup_num = 0
  set_of_chars = set()
  for char in txt:
    if char in set_of_chars:
      dup_num += 1
    set_of_chars.add(char)
    
  return dup_num

