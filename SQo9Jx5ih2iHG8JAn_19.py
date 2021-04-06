
def expanded_form(num):
  num = str(num)
  ans = []
  for i in range(len(num)):
    x = num[i] + '0'*(len(num)-i-1)
    if int(x) != 0: ans += [x]
  return ' + '.join(ans)

