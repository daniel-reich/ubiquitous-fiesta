
def fizz_buzz(maximum):
  solution = []
  
  for n in range(1,maximum+1):
    if (n % 3 == 0 and n % 5 == 0):
      solution.append("FizzBuzz")
    elif (n % 3 == 0):
      solution.append("Fizz")
    elif (n % 5 == 0):
      solution.append("Buzz")
    else:
      solution.append(n)
  
  return solution

