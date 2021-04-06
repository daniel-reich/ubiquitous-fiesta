
def fractionizer (fraction):
  result,temp,denominators,i= 0,fraction,[],1
  while not round(result,len(str(fraction))-2) == fraction:
    if result+1/(2**i)<= fraction:
      denominators.append(2**i)
      result+=1/(2**i)
      temp-=result
    i+=1
  return denominators
​
def binary_sum(lst):
  first,second=[0,0],[0,0]
  first[0],first[1]=lst[0].split('.')[0],lst[0].split('.')[1]
  second[0],second[1]=lst[1].split('.')[0],lst[1].split('.')[1]
  whole =sum([2**(len(first[0])-1-i) for i in range (len(first[0])) if first[0][i]=='1'])+\
  sum([2**(len(second[0])-1-i) for i in range (len(second[0])) if second[0][i]=='1'])
  fraction= sum([2**(-i-1) for i in range (len(first[1])) if first[1][i]=='1'])+\
  sum([2**(-i-1)  for i in range (len(second[1])) if second[1][i]=='1'])
  if fraction>=1:
    whole,fraction=whole+1,fraction-1
  if fraction == 0:
    return str(whole)
  denominators=fractionizer (fraction)
  lcd=max(denominators)
  numerator=0
  for i in range(len(denominators)):
    numerator+=lcd//denominators[i]
  return str(whole) + ' ' + str(numerator) + '/' + str(lcd) if whole >0 else str(numerator) + '/' + str(lcd)

