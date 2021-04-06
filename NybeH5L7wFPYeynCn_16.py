
def three_letter_collection(s):
  if len(s)<3:
    return []
  return sorted([s[i:i+3] for i in range(len(s)-2)])

