
def three_letter_collection(s):
  return sorted(s[i:i + 3] for i in range(len(s) - 2))

