
def is_smooth(sentence):
  s = sentence.lower().split()
  return  all(s[i][-1] == s[i+1][0] for i in range(len(s) - 1))

