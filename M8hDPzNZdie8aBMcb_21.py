
def count_substring(s):
  return sum(s[i:].count("X") for i in range(len(s)) if s[i]=="A")

