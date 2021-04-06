
def find_even_nums(num):
  j = []
  for i in range(1,num+1,1):
    if i%2==0:
      j.append(i)
  return j

