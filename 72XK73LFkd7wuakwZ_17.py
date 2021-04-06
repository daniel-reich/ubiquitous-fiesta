
def junction_or_self(n):
  def does_it_add(testnum, targnum):
    digits = list(str(testnum))
    d = []
    for digit in digits:
      d.append(int(digit))
    digits = d
    del d
    
    su = testnum + sum(digits)
    
    return su == targnum
  
  validnums = []
  for num in range(1, n):
    dia = does_it_add(num, n)
    if dia == True:
      validnums.append(num)
  
  if validnums == []:
    return 'Self'
  else:
    return list(reversed(sorted(validnums)))

