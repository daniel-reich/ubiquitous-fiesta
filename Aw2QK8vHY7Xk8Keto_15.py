
def longest_word(s):
  max = 0
  cnt = " "
  x = s.split()
  for i in range(len(x)):
    z = len(x[i])
    if z > max:
      max = z
      cnt = x[i]
  return cnt
print(longest_word("A thing of beauty is a joy forever."))

