
def third_most_expensive(dct):
  if len(dct)<3:
    return False
  return sorted(dct.items(),key=lambda x:x[1],reverse=True)[2][0]

