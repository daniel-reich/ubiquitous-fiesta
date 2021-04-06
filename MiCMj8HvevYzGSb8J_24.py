
def fibo_word(n):
  fw = ['b', 'a']
  for i in range(2, n):
    fw.append(fw[i-1] + fw[i-2])
  return ', '.join(fw) if n >1 else 'invalid'

