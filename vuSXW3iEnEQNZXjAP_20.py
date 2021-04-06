
def create_square(n):
  arr = []
  if n==None or n <= 0:
    return ''
  elif n == 1:
    return '#'
  else:
    arr.append(n*'#')
    for i in range(n-2):
      arr.append('#'+(' '*(n-2)+ '#'))
    arr.append(n*'#')
  return '\n'.join(arr)

