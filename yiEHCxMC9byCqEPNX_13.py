
def is_palindrome(p):
  sidha = ""
  for char in p:
    if char.isalpha():
      sidha+=char
  sidha = sidha.lower()
  ulta = sidha[::-1]
  return sidha==ulta

