
def expanded_form(num):
  lst = [int(n)*10**i for i, n in enumerate(str(num)[::-1])]
  return ' + '.join(str(i) for i in lst[::-1] if i)

