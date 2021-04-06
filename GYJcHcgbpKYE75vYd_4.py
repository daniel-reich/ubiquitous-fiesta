
def return_end_of_number(num):
  if num == 1 or num % 100 > 20 and num % 10 == 1:
    return '{}-ST'.format(num)
  if num == 2 or num % 100 > 20 and num % 10 == 2:
    return '{}-ND'.format(num)
  if num == 3 or num % 100 > 20 and num % 10 == 3:
    return '{}-RD'.format(num)
  return '{}-TH'.format(num)

