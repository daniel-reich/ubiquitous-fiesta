
def in_alpha(word):
  total = 0
  for i in word:
    if i.isalpha():
      total += ord(i.lower()) - 64
    else:
      total += 1
  return total % 2 == 0

