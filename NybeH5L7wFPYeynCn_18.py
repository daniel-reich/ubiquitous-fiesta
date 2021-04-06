
def three_letter_collection(s):
  result = []
  if len(s) <= 2:
    return result
  for i in range(len(s)):
    result.append(s[i:3+i])
    if 3+i >= len(s):
      break
  return sorted(result)

