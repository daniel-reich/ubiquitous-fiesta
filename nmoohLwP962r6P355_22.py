
def straight_digital(number):
  if number<100: return 'Not Straight'
  if str(number)[0]==str(number)[1]: return 'Trivial Straight'
  for i in range(len(str(number))-1):
    if int(str(number)[i])-int(str(number)[i+1])!=int(str(number)[0])-int(str(number)[1]):
      return 'Not Straight'
  return int(str(number)[1])-int(str(number)[0])

