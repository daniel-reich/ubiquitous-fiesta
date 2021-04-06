
def eng2nums(s):
  ones={ 'one':   1, 'eleven':     11,
       'two':   2, 'twelve':     12,
       'three': 3, 'thirteen':   13,
       'four':  4, 'fourteen':   14,
       'five':  5, 'fifteen':    15,
       'six':   6, 'sixteen':    16,
       'seven': 7, 'seventeen':  17,
       'eight': 8, 'eighteen':   18,
       'nine':  9, 'nineteen':   19,
       'zero':  0}
  tens={ 'ten':     10,
       'twenty':  20,
       'thirty':  30,
       'forty':   40,
       'fifty':   50,
       'sixty':   60,
       'seventy': 70,
       'eighty':  80,
       'ninety':  90 }
  A=s.split()
  res=''
  for x in A:
    if x in ones:
      res+='+'+str(ones[x])
    elif x in tens:
      res+='+'+str(tens[x])
    else:
      res+='*100'
  if res[0]=='+':
    res=res[1:]
  return eval(res)

