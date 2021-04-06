
def power_morphic(num):
  count = 0
  for k in range (2,11):
    if str(num) == str(num**k)[-len(str(num)):]: count += 1
  dic = {'9': "Polymorphic", '87654': "Quadrimorphic", '32': "Dimorphic", '1': "Enamorphic", '0': "Amorphic"}
  return ''.join([v for k, v in dic.items() if str(count) in k])

