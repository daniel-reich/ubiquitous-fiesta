
def apocalyptic(n):
  n = str(2**n)
  count = 0
  for i in range(0, len(n), 1):
    if n[i]=='6':
      count=count+1
      if count == 3:
        return 'Repent! ' + str(i-2) + ' days until the Apocalypse!'
    else:
      count = 0
  return 'Crisis averted. Resume sinning.'

