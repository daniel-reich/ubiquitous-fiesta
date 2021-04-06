
def lengthen(s1, s2):
  lst= [len(s1),len(s2)]
  num = max(lst)//min(lst)
  part= max(lst)%min(lst)
  if len(s1) > len(s2) :compaunder = s2
  elif  len(s1) <  len(s2) :compaunder = s1
  else: compaunder = ''
  result=''
  for i in range(num):
    result = result +compaunder
  result = result + compaunder[:part]
  return result

