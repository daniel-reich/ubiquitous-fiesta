
def apocalyptic(n):
  num=str(2**n)
  for i in range(len(num)-3):
    if num[i]=='6' and num[i+1]=='6' and num[i+2]=='6':
      return "Repent! {} days until the Apocalypse!".format(i)
  return "Crisis averted. Resume sinning."

