
def fruit_salad(lst):
  return ''.join(sorted(sum([[i[0:len(i) // 2], i[len(i)//2:]] for i in lst], [])))

