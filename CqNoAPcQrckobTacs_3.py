
def missing_letter(lst):
  
  a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z' + ' a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper()
  a = a.split()
  
  indexes = []
  
  for l8r in lst:
    for n in range(0, len(a)):
      tl8r = a[n]
      if tl8r == l8r:
        indexes.append(n)
  
  indexes = sorted(indexes)
  
  wanted = []
  
  for n in range(indexes[0], indexes[-1] + 1):
    wanted.append(a[n])
  
  for item in wanted:
    if item not in lst:
      return item

