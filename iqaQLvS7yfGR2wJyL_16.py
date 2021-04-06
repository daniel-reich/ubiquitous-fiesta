
def num_of_digits(num):
  x=0
  for i in str(num):
    if i.isnumeric():
      x+=1
  return x

