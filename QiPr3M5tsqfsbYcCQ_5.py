
def square_digits(n):
  lst = list(str(n))
  lst = [(int(x)*int(x)) for x in lst]
  return int("".join([str(x) for x in lst]))

