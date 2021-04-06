
def maya_number(n):
  if not n: return ['@']
  def symb(num):
    if not num: return '@'
    s = ''
    s += '-'*(num//5)
    num -= 5*(num//5)
    s += 'o'*num
    return ''.join(p for p in sorted(s, reverse = True))
  i = 0
  while 19*(20**i) < n: i+=1
  symbs = []
  while i != -1:
    symbs.append(symb(n//(20**i)))
    n -= (n//(20**i))*(20**i)  # x * 20 ** y
    i -= 1
  return symbs

