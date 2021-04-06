
def is_palindrome(p):
  # your recursive solution here
  A=[x.lower() for x in p if x.isalpha()]
  
  if len(p)<2:
    return True
  else:
    return A[0]==A[-1] and is_palindrome(''.join(A[1:-1]))

