
def uncensor(txt, vowels):
  it = 0
  ans = ''
  for i in txt:
    if i == '*':
      ans += vowels[it]
      it += 1
    else:
      ans += i
  return ans

