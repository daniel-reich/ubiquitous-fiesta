
def fizz_buzz(maximum):
  ans = []
  for i in range(1,maximum+1):
    if i % 3 == 0 and i % 5 == 0:
      ans.append('FizzBuzz') 
    elif i % 3 == 0:
      ans.append('Fizz')
    elif i % 5 == 0:
      ans.append('Buzz') 
    else:
      ans.append(i) 
  return ans

