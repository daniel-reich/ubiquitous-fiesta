
def is_harshad(num):
  sum_of_digits  =  sum(int(x) for x in str(num))
  return num%sum_of_digits == 0 if sum_of_digits > 0 else False

