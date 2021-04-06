
def three_letter_collection(s):
  groupings = [s[i:i+3] for i in range(len(s)-2)]
  return sorted(groupings)

