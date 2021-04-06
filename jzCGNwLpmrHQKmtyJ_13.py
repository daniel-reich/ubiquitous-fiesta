
def parity_analysis(num):
  list_num = list(str(num))
  sum_num = sum([int(n) for n in list_num])
  if (sum_num % 2 == 0 and num % 2 == 0) or (sum_num % 2 != 0 and num % 2 != 0):
    return True
  return False

