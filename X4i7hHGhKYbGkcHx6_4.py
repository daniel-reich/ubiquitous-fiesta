
def average_index(l):
  a = [chr(i) for i in range(ord('a'),ord('z')+1)]
  return round(sum([a.index(i)+1 for i in l if i in a])/len(l), 2)

