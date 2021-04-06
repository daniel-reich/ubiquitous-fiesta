
def fizz_buzz(maximum):
​
  returnlist = []
​
  for a in range(1, maximum+1):
    if (a % 5 == 0) & (a % 3 == 0):
      returnlist.append('FizzBuzz')
    elif a % 5 == 0:
      returnlist.append('Buzz')
    elif a % 3 == 0:
      returnlist.append('Fizz')
    else:
      returnlist.append(a)
      
  return returnlist

