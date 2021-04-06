
def mathematical(exp, numbers):
  res = []
  exp = exp.replace("^","**")
  exp = exp.replace("x","*")
  var = exp[2]
  for num in numbers:
    exp_out = exp.replace(var,str(num))
    left,right = exp_out.split("=")
    ans = int(eval(right))
    res.append("%s=%s"%(left,ans))
  return res

