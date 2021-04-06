
def generate_palindromes(limit):
  list1 = []
  for x in range(11,limit+1):
    if str(x) == str(x)[-1::-1]:
      list1.append(x)
  return list1[-15:]

