
def fruit_salad(fruits):
  lst = []
  half = lambda x: len(x) // 2
  for i in fruits:    
    lst.extend((i[:half(i)], i[half(i):]))
  return ''.join(sorted(lst))

