
def even_odd_transform(lst, n):
  return [i + n*2 if i%2 else i - n*2 for i in lst]

