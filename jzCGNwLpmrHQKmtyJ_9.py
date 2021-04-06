
def parity_analysis(num):
  num_parity = ("O" if num % 2 != 0 else "E")
  s = str(num)
  s = [int(i) for i in s]
  sum_parity = ("O" if sum(s) % 2 != 0 else "E")
  return True if num_parity == sum_parity else False

