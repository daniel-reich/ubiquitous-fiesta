
def is_palindrome(n):
  forward = str(n)
  backward = ''
  for i in range(len(forward)-1, -1, -1):
    backward += forward[i]
  if forward == backward:
    return True
  return False
​
def palindrome_descendant(n):
  all_descendants = [str(n)]
  while len(all_descendants[-1]) % 2 == 0:
    next_number = ''        
    for i in range(0, len(all_descendants[-1]), 2):
      next_number += str( int(all_descendants[-1][i]) + int(all_descendants[-1][i+1]) )
    all_descendants.append(next_number)
  for number in all_descendants:
    if is_palindrome(int(number)) and len(number) > 1.5:
      return True
  return False

