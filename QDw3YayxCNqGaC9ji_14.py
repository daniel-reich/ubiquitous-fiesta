
def make_change(c):
  change_dict = {}
  remainder = c%25
  change_dict['q'] = abs(int((c - remainder)/25))
  remainder1 = remainder%10
  change_dict['d'] = abs(int((remainder1 - remainder)/10))
  remainder2 = remainder1%5
  change_dict['n'] = abs(int((remainder2 - remainder1)/5))
  remainder3 = remainder2%1
  change_dict['p'] = abs(int(remainder3 - remainder2))
  return change_dict

