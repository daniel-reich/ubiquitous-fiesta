
def generate_palindromes(limit):
  def isPalindrome(n):
    s = str(n)
    for i in range(len(s)//2):
      if s[i] != s[-i-1]:
        return False
    return True
    
  count = 0
  lst = []
  while count < 15 and limit > 0:
    if isPalindrome(limit):
      lst.insert(0, limit)
      count += 1
    limit -= 1
  return lst

