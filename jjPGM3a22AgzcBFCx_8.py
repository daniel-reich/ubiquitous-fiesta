
def decrypt(lst):
  letter = set(list(range(1, 27))) - set(lst)
  return chr(letter.pop() + 64)

