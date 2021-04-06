
def verbify(txt):
  converted=txt.split()
  ans=""
  if converted[0][-2:]=="ed":
    return txt
  elif converted[0][-1]=="e":
    ans+=converted[0]+"d "+converted[1]
    return ans
  else:
    ans+=converted[0]+"ed "+converted[1]
    return ans

