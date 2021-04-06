
def third_most_expensive(dct):
  if len(dct)<3:
    return False
  else:
    ls=sorted(dct.items(),key=lambda d:d[1],reverse=True)
    return ls[2][0]

