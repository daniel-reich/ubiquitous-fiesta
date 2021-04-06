
def frac_round(frac, n):
  ans = str(round(eval(frac),n))
  if len(ans[ans.index(".")+1:])<n:
    for i in range(0,(n-len(ans[ans.index(".")+1:]))):
      ans=ans+"0"
  return frac+" rounded to "+str(n)+" decimal places is "+ans

