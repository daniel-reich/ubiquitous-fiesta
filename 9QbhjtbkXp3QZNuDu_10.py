
def generate_palindromes(limit):
  lst = []
  while len(lst) != 15:
    if str(limit) == str(limit)[::-1]:
      lst.append(limit)
    limit -= 1
  lst.reverse()
  return lst

