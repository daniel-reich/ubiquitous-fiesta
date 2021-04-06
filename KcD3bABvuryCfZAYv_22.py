
def most_frequent_char(lst):
  lst_string = ''.join(lst)
  counts = []
  chars = []
  for i in lst_string:
    counts.append(lst_string.count(i))
  for i in lst_string:
    if lst_string.count(i) == max(counts):
      chars.append(i)
  return sorted(set(chars))

