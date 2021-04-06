
def trouble(num1, num2):
  chars = set([x for x in str(num1) if str(num1).count(x)>=3 and str(num2).count(x)>=2])
  return [x*3 in str(num1) and x*2 in str(num2) for x in chars][0] if chars else False

