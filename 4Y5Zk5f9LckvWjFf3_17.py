
def special_reverse(s, c):
  result = []
  for i in s.split():
    if i[0] == c:
      result.append(i[::-1])
    else:
      result.append(i)
  return ' '.join(result)

