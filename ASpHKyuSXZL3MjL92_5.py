
def amplify(num):
  return [ x if x % 4 !=0 else x*10 for x in range(1,num+1) ]

