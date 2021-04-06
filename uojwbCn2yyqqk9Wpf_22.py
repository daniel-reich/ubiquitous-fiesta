
def is_untouchable(number):
  def divisors(number):
    divs = []
    for n in range(1, int(number/2) + 1):
      r = number % n
      if r == 0:
        divs.append(n)
    return divs
  
  if number < 2:
    return "Invalid Input"
​
  numbers = []
  
  for n in range(2, number ** 2):
    if sum(divisors(n)) == number:
        numbers.append(n)
  
  if len(numbers) == 0:
    return True
  else:
    return numbers

