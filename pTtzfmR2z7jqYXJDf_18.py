
def possible_palindrome(s):
  n = [s.count(c)%2 for c in set(s)].count(1)
  return n==1 or (n==0 and len(s)%2==0)

