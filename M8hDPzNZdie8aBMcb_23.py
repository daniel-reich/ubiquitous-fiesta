
def count_substring(s):
  result = 0
  for i in range(len(s) - 1):
    for j in range(i, len(s)):
      if s[i] == "A" and s[j] == "X":
        result += 1
  return result

