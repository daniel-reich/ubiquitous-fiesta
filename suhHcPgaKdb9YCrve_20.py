
def even_or_odd(s):
  even=sum([int(i) for i in s if int(i)%2==0])
  odd=sum([int(i) for i in s if int(i)%2])
  if even<odd:return 'Odd is greater than Even'
  elif even>odd:return 'Even is greater than Odd'
  else:return 'Even and Odd are the same'

