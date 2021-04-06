
def is_palindrome_possible(txt):
  if len(txt) %2: return [str(txt.count(x)%2) for x in set(txt)].count('1')== 1
  else : return all(not txt.count(x) % 2 for x in txt)

