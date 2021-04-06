
def count_substring(s):
  return sum(s[i+1:].count("X") if l=="A" else 0 for i,l in enumerate(s[:-1]))

