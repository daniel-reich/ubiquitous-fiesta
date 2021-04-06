
def list_between(num1, num2, lst):
  new=[]
  for i in lst:
    if i>num1 and i<num2:
      new.append(i)
  return new

