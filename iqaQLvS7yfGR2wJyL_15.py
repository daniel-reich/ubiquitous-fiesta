
def num_of_digits(num):
  a = 0
  for i in range(len(str(num))):
    if str(num)[i].isdigit():
      a += 1
  return a

