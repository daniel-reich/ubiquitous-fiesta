
def three_letter_collection(s):
  return sorted(s[i:i+3] for i in range(0, len(s)) if len(s[i:i+3]) > 2)

