
def get_birthday_cake(n, a):
  c = ['#','*'][a%2]
  s = c+" {} Happy Birthday {}! {} ".format(a,n,a)+c
  l = len(s)
  return [c*l]+[s]+[c*l]

