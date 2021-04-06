
def return_end_of_number(num):
  if len(str(num)) >= 2:
    if str(num)[-2] == '1': return '{}-TH'.format(str(num).upper())
  if str(num)[-1] == '1': return '{}-ST'.format(str(num).upper())
  if str(num)[-1] == '3': return '{}-RD'.format(str(num).upper())
  if str(num)[-1] == '2': return '{}-ND'.format(str(num).upper())
  return '{}-TH'.format(str(num).upper())

