
def sum_round(num):
  m = 10
  lst = []
  while m<num*10:
    lst.append(str((num%m)-(num%(m//10))))
    m*=10
  return ' '.join([i for i in lst if i!='0'])

