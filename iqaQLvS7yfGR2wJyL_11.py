
def num_of_digits(num):
  return len(str(num)) -1 if str(num).startswith('-') else len(str(num))

