
def expanded_form(num):
  digits = list(enumerate(str(num)))
  length = len(digits)
  lst = ['{}{}'.format(digit, '0' * (length - (index + 1))) for index, digit in digits if digit != '0']
  return ' + '.join(lst)

