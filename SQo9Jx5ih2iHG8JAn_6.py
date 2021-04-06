
def expanded_form(num):
  num = str(num)
  return ' + '.join(x + '0' * (len(num)-i-1) for i, x in enumerate(num) if x != '0')

