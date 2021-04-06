
def generate_palindromes(limit):
  ctr = 0
  myans = []
  while ctr < 15:
    temp = str(limit)
    if temp == temp[::-1]:
      ctr += 1
      myans.append(limit)
    limit -= 1
  return sorted(myans)

