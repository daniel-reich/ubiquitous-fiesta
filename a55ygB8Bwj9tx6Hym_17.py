
def steps_to_convert(txt):
  lower,upper='',''
  lower_case,upper_case=0,0
  for i in txt:
    if i.isupper():
      lower+=i.lower()
      lower_case+=1
    else:
      lower+=i
  for i in txt:
    if i.islower():
      upper+=i.upper()
      upper_case+=1
  return min(lower_case,upper_case)

