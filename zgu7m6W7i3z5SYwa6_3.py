
def is_equal(lst):
  num1=str(lst[0])
  num2=str(lst[1])
  total1=0
  total2=0
  for i in num1:
    total1+=int(i)
  for i in num2:
    total2+=int(i)
  return total1==total2

