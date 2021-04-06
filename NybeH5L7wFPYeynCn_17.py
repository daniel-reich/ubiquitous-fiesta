
def three_letter_collection(s):
  if len(s) < 3:
    return []
  return sorted([s[x:x+3] for x in range(len(s) - 2)])

