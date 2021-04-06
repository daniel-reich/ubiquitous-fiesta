
def decrypt(lst):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(1, 27):
    if i not in lst: return letters[i - 1]

