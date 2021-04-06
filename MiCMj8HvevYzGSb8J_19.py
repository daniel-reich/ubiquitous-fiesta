
def fibo_word(n):
  if n<2:
    return 'invalid'
  i=['b','a']
  for j in range(n-2):
    i.append(i[-1]+i[-2])
  str=''
  for k in range(len(i)-1):
    str+=i[k]
    str+=', '
  str+=i[-1]
  return str

