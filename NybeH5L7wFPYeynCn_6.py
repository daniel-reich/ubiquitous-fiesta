
def three_letter_collection(s):
  return sorted(a+b+c for a,b,c in zip(s, s[1::], s[2::]))

