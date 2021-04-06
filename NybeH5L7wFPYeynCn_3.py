
def three_letter_collection(s):
  length = len(s)
  res = []
  if length < 3:
    return res
  for i in range(0, length -2):
    res.append(s[i:i+3])
  res.sort()
  return res

