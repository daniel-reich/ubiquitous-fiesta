
def ABA(s):
  import string
  alphabet = string.ascii_uppercase
  i = alphabet.find(s)
​
  if s == 'A':
    return 'A'
  return ABA(alphabet[i-1]) + alphabet[i] + ABA(alphabet[i-1])

