
def divisible_by_left(n):
  return [False]+[False if str(n)[i-1]=='0' else int(str(n)[i])%int(str(n)[i-1])==0 for i in range(1,len(str(n)))]

