
def ulam(n):
  numbers = [1, 2]
  current = 3
  
  while len(numbers) < n:
    found_distinct_summands = 0
    
    for number in numbers:
      if current - number in numbers and number != current / 2:
        found_distinct_summands += 1
        
      if found_distinct_summands > 2:
        break;
        
    if found_distinct_summands == 2:
      numbers.append(current)
      
    current += 1
    
  return numbers[-1]

