
def describe_num(n):
  w = 'The most brilliant'
  if n%2==0:w+=' exciting'
  if n%3==0:w+=' fantastic'
  if n%4==0:w+=' virtuous'
  if n%5==0:w+=' heart-warming'
  if n%6==0:w+=' tear-jerking'
  if n%7==0:w+=' beautiful'
  if n%8==0:w+=' exhilarating'
  if n%9==0:w+=' emotional'
  if n%10==0:w+=' inspiring'
  return w+' number is '+str(n)+'!'

