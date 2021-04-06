
def gimme_the_letters(s):
  a, z = s[0], s[2]
  return ''.join(chr(i) for i in range(ord(a), ord(z)+1))

