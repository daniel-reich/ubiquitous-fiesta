
def most_frequent_char(lst):
  chars = ''.join(lst)
  return sorted(i for i in set(chars) if chars.count(i)==max(chars.count(j) for j in chars))

