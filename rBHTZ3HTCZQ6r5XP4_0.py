
def expanded_form(num):
  a, b = str(num).split('.')
  lst1 = [x + '0' * (len(a) - i - 1) for i, x in enumerate(a) if x != '0']
  lst2 = ["{}/1{}".format(x, '0' * (i + 1)) for i, x in enumerate(b) if x != '0']
  return ' + '.join(lst1 + lst2)

