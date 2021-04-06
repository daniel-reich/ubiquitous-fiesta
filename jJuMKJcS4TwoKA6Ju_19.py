
def dial(txt):
  ans=''
  for i in txt:
    if i.isalpha():
      if i in 'abcABC':ans+='2'
      elif i in 'DEFdef':ans+='3'
      elif i in 'GHIghi':ans+='4'
      elif i in 'JKLjkl': ans+='5'
      elif i in 'MNOmno':ans+='6'
      elif i in 'PQRSpqrs':ans+='7'
      elif i in 'TUVtuv':ans+='8'
      elif i in 'WXYZwxyz':ans+='9'
    else:ans+=i
  return ans

