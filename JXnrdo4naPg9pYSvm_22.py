
def frac_round(frac, n):
  decimal = eval(frac)
  rounded_decimal = str(round(decimal, n))
  split_number = rounded_decimal.split(".")
  if n > len(split_number[1]):
    rounded_decimal = split_number[0] + "." + split_number[1] + "0" * (n - len(split_number[1]))
  return "%s rounded to %d decimal places is %s" % (frac, n, rounded_decimal)

