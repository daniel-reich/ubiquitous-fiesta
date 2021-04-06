
def count_substring(s):
  return sum(s[i:].count("X") for i,c in enumerate(s) if c=="A")

