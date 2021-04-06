
def DECIMATOR(txt):
  return txt[:-(len(txt)//10)] if len(txt)%10==0 else txt[:-(1+(len(txt)//10))]

