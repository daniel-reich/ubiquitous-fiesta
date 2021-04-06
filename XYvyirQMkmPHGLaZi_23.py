
def boom_intensity(n):
  print(n)
  mystr= 'o'
  if n<2:
    return 'boom'
  x = (mystr*n)
  print(x)
  if n%2==0 and n%5!=0:
    ans = 'B'+x+'m!'
    return ans
  elif n%5==0 and n%2!=0:
    ans = ('B'+x+'m')
    print(ans)
    ans = ans.upper()
    print(ans)
    return ans
  elif n %2==0 and n%5==0:
    ans = ('B'+x+'m!')
    ans = ans.upper()
    return ans
  else:
    return 'B'+x+'m'

