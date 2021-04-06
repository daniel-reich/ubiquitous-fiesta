
def longest_substring(digits):
​
  def is_even(n):
    return (int(n) % 2) == 0
    
  longest = ''
  current = ''
  was_even = not is_even(digits[0])
  
  while digits:
    while digits and ((was_even and (not is_even(digits[0]))) or 
                      ((not was_even) and is_even(digits[0]))):
      current += digits[0]
      was_even = is_even(digits[0])
      digits = digits [1:]
    if len(current) > len(longest):
      longest = current
    current = ''
    was_even = not was_even
      
  return longest

