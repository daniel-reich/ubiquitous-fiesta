
def min_palindrome_steps(s):
  for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
      return i

