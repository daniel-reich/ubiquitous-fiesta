
def is_zygodrome(num):
  num = str(num)+'%'
  a = list(num[i] if num[i]==num[i+1] else num[i]+'%' for i in range(len(num)-1))
  b = list(len(i) for i in "".join(a).split('%'))[:-1]
  return False if min(b)<2 else True

