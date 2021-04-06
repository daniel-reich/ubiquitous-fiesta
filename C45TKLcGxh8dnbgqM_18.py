
from string import ascii_lowercase as a
from string import ascii_uppercase as b
def caesar_cipher(s, k):
  return ''.join([a[(ord(x)-97+k)%26] if x.islower() else b[(ord(x)-65+k)%26] if x.isupper() else x for x in s])

