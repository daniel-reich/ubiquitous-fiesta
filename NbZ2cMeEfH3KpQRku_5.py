
def portion_happy(numbers):
  n,n1,n2 =  numbers,numbers[1:]+[2],[2]+numbers[:-1]
  return sum(x in [y,z] for (x,y,z) in zip(n,n1,n2))/len(numbers)

