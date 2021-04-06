
def count_digits(lst, t):
  result = []
  
  for element in lst:
    count = 0
    for digit in str(element):
      if t == "even" and int(digit)%2 == 0:
        count += 1
      if t == "odd" and int(digit)%2 != 0:
        count += 1
    result.append(count)
    
  return result

