
def decrypt(lst):
  return chr(ord('A') + (set(range(1, 26)) - set(lst)).pop() - 1)

